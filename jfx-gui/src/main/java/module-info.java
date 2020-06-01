module org.ibtc.ibtc {
    requires javafx.controls;
    requires javafx.fxml;
	requires java.desktop;
	requires javafx.graphics;
	requires com.jfoenix;
	requires javafx.base;

    opens org.ibtc.ibtc to javafx.fxml;
    exports org.ibtc.ibtc;
}