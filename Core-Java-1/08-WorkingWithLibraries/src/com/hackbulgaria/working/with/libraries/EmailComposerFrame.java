package com.hackbulgaria.working.with.libraries;

import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class EmailComposerFrame extends JFrame {
    private static final long serialVersionUID = -5237971748643708877L;
    private static final int FRAME_WIDTH = 300;
    private static final int FRAME_HEIGHT = 300;
    private JTextField fromField;
    private JTextField subjectField;
    private JTextField toField;
    private JTextArea messageArea;
    private CardLayout cardLayout;
    private JPanel corePanel;
    private static final int FIELD_SIZE = 10;

    private static final String DEFAULT_SMTP_HOSTNAME = "smtp.gmail.com";
    private static final int DEFAULT_SMTP_PORT = 465;
    private JTextField smtpHostName = new JTextField(FIELD_SIZE);
    private JTextField smtpPort = new JTextField(FIELD_SIZE);
    private JTextField usernameField = new JTextField(FIELD_SIZE);
    private JTextField passwordField = new JPasswordField(FIELD_SIZE);
    private String attachmentPath = "";

    public EmailComposerFrame() {
        this.renderComponents();
        super.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        super.setSize(FRAME_WIDTH, FRAME_HEIGHT);
        super.setVisible(true);
    }

    private void renderComponents() {
        this.cardLayout = new CardLayout();
        this.corePanel = new JPanel(this.cardLayout);
        this.corePanel.add(this.renderSettingsPanel(), "settingsPanel");
        this.corePanel.add(this.renderComposeEmailPanel(), "composeEmailPanel");
        this.cardLayout.show(this.corePanel, "settingsPanel");
        super.add(this.corePanel);
    }

    private JPanel renderSettingsPanel() {
        JPanel usernamePanel = new JPanel();
        usernamePanel.add(new JLabel("Username:"));
        usernamePanel.add(this.usernameField);
        JPanel passwordPanel = new JPanel();
        passwordPanel.add(new JLabel("Password:"));
        passwordPanel.add(this.passwordField);
        JPanel settingsPanel = new JPanel();
        settingsPanel.add(new JLabel("SMTP hostname: "));
        this.smtpHostName.setText(DEFAULT_SMTP_HOSTNAME);
        settingsPanel.add(this.smtpHostName);
        settingsPanel.add(new JLabel("SMTP Port: "));
        this.smtpPort.setText(String.valueOf(DEFAULT_SMTP_PORT));
        settingsPanel.add(this.smtpPort);
        JPanel mainPanel = new JPanel(new GridLayout(4, 1));
        JButton continueButton = new JButton("Continue!");
        continueButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                EmailComposerFrame.this.cardLayout.show(EmailComposerFrame.this.corePanel, "composeEmailPanel");
            }
        });
        mainPanel.add(usernamePanel);
        mainPanel.add(passwordPanel);
        mainPanel.add(settingsPanel);
        mainPanel.add(continueButton);
        return mainPanel;
    }

    private JPanel renderComposeEmailPanel() {
        this.fromField = new JTextField(FIELD_SIZE);
        JPanel fromPanel = new JPanel();
        fromPanel.add(new JLabel("From:"));
        fromPanel.add(this.fromField);

        JPanel toPanel = new JPanel();
        this.toField = new JTextField(FIELD_SIZE);
        toPanel.add(new JLabel("To:"));
        toPanel.add(this.toField);

        JPanel emailPanel = new JPanel(new BorderLayout());
        this.subjectField = new JTextField(FIELD_SIZE);
        this.messageArea = this.createTextArea();
        emailPanel.add(this.subjectField, BorderLayout.NORTH);
        emailPanel.add(this.messageArea, BorderLayout.CENTER);
        JPanel subjectPanel = new JPanel();
        subjectPanel.add(new JLabel("Subject:"));
        subjectPanel.add(this.subjectField);
        JPanel buttonPanel = new JPanel();
        JButton backButton = new JButton("Back!");
        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                EmailComposerFrame.this.cardLayout.show(EmailComposerFrame.this.corePanel, "settingsPanel");
            }
        });
        JButton attachmentButton = new JButton("Attachment");
        attachmentButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                int r = fileChooser.showOpenDialog(new JFrame());
                if (r == JFileChooser.APPROVE_OPTION) {
                    EmailComposerFrame.this.attachmentPath = fileChooser.getSelectedFile().getPath();
                }
            }
        });
        JButton sendButton = new JButton("Send!");
        sendButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (EmailComposerFrame.this.attachmentPath.isEmpty()) {
                    EmailUtils.sendEmail(EmailComposerFrame.this.smtpHostName.getText(),
                            Integer.valueOf(EmailComposerFrame.this.smtpPort.getText()),
                            EmailComposerFrame.this.usernameField.getText(),
                            EmailComposerFrame.this.passwordField.getText(),
                            EmailComposerFrame.this.fromField.getText(), EmailComposerFrame.this.toField.getText(),
                            EmailComposerFrame.this.subjectField.getText(),
                            EmailComposerFrame.this.messageArea.getText());
                } else {
                    EmailUtils.sendEmail(EmailComposerFrame.this.smtpHostName.getText(),
                            Integer.valueOf(EmailComposerFrame.this.smtpPort.getText()),
                            EmailComposerFrame.this.usernameField.getText(),
                            EmailComposerFrame.this.passwordField.getText(),
                            EmailComposerFrame.this.fromField.getText(), EmailComposerFrame.this.toField.getText(),
                            EmailComposerFrame.this.subjectField.getText(),
                            EmailComposerFrame.this.messageArea.getText(),
                            EmailUtils.addAttachment(EmailComposerFrame.this.attachmentPath));
                }
            }
        });
        buttonPanel.add(backButton);
        buttonPanel.add(attachmentButton);
        buttonPanel.add(sendButton);
        JPanel mainPanel = new JPanel(new GridLayout(5, 1));
        mainPanel.add(fromPanel);
        mainPanel.add(toPanel);
        mainPanel.add(subjectPanel);
        mainPanel.add(emailPanel);
        mainPanel.add(buttonPanel);
        return mainPanel;
    }

    private JTextArea createTextArea() {
        JTextArea textArea = new JTextArea(10, 20);
        textArea.setEditable(true);
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);
        return textArea;
    }
}
