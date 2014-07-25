package com.hackbulgaria.working.with.libraries;

import org.apache.commons.mail.Email;
import org.apache.commons.mail.EmailAttachment;
import org.apache.commons.mail.EmailException;
import org.apache.commons.mail.MultiPartEmail;
import org.apache.commons.mail.SimpleEmail;

public class EmailUtils {
    public static void sendEmail(String smtpHostName, int smtpPort, String authName, String authPassword,
            String fromEmail, String toEmail, String subject, String message, EmailAttachment attachment) {
        MultiPartEmail email = new MultiPartEmail();
        email.setHostName(smtpHostName);
        email.setSmtpPort(smtpPort);
        email.setSSLOnConnect(true);
        email.setAuthentication(authName, authPassword);
        try {
            email.setFrom(fromEmail, toEmail);
            email.setSubject(subject);
            email.setMsg(message);
            email.addTo(toEmail);
            email.attach(attachment);
            email.send();
        } catch (EmailException e) {
            System.out.println("Invalid authentication");
            e.printStackTrace();
        }
    }

    public static void sendEmail(String smtpHostName, int smtpPort, String authName, String authPassword,
            String from_email, String to_email, String subject, String message) {
        Email email = new SimpleEmail();
        email.setHostName(smtpHostName);
        email.setSmtpPort(smtpPort);
        email.setSSLOnConnect(true);
        email.setAuthentication(authName, authPassword);
        try {
            email.setFrom(from_email, to_email);
            email.setSubject(subject);
            email.setMsg(message);
            email.addTo(to_email);
            email.send();
        } catch (EmailException e) {
            System.out.println("Invalid authentication");
            e.printStackTrace();
        }
    }

    public static EmailAttachment addAttachment(String path, String description, String name) {
        EmailAttachment attachment = new EmailAttachment();
        attachment.setPath(path);
        attachment.setDisposition(EmailAttachment.ATTACHMENT);
        attachment.setDescription(description);
        attachment.setName(name);
        return attachment;
    }

    public static EmailAttachment addAttachment(String path, String description) {
        return addAttachment(path, description, "");
    }

    public static EmailAttachment addAttachment(String path) {
        return addAttachment(path, "", "");
    }
}
