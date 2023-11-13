package com.example.demo;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.InetSocketAddress;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        Label texto = new Label("Bienvenido esta es la primer Scene");

        Button boton = new Button("ir a la scene 2");

        VBox vBox = new VBox(20);
        vBox.getChildren().addAll(texto, boton);

        Scene scene = new Scene(vBox, 300, 200);

        stage.setScene(scene);
        stage.show();


        /*
        FlowPane root = new FlowPane();

        stage.setTitle("Titulo");

        Button boton = new Button("Ir a scene 2");
        root.getChildren().add(boton);

        Label texto = new Label("Bienvenido esta es la primer Scene");
        root.getChildren().add(texto);


        Scene scene = new Scene(root, 300,200);
        stage.setScene(scene);
        stage.show();
        */

    }

    public static void main(String[] args) {
        launch(args);
    }
}