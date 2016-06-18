SET client_encoding = 'UTF8';
CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
SET search_path = public, pg_catalog;
SET default_tablespace = '';
SET default_with_oids = false;
CREATE TABLE tab_canaima_c (
    serial_c character varying(18) NOT NULL,
    modelo_c character varying(4),
	institucion_c text,
    ci_n integer NOT NULL
);
CREATE TABLE tab_nino_n (
    ci_n integer NOT NULL,
    nombre_n text NOT NULL,
    plantel_n text,
    nivel_n character varying(8),
    municipio_n text NOT NULL,
    ci_r integer NOT NULL
);
CREATE TABLE tab_reparacion_re (
    id_re character varying(30) NOT NULL,
    fec_re_re character varying(10) NOT NULL,
    fec_en_re character varying(10),
    falla_re text NOT NULL,
    act_re character(2),
    reparada_re character(2),
    entregada_re character(2),
    cambio_re character(2),
    centro_re text NOT NULL,
    serial_c character varying(18) NOT NULL
);
CREATE TABLE tab_representante_r (
    ci_r integer NOT NULL,
    nombre_r text NOT NULL,
    tlf_r character varying(11)
);
CREATE TABLE tab_canaima_representante_cr (
    id_cr character varying(30) NOT NULL,
    ci_r integer NOT NULL,
    serial_c character varying(18) NOT NULL
);
ALTER TABLE ONLY tab_canaima_c
    ADD CONSTRAINT tab_canaima_c_pkey PRIMARY KEY (serial_c);
ALTER TABLE ONLY tab_nino_n
    ADD CONSTRAINT tab_nino_n_pkey PRIMARY KEY (ci_n);
ALTER TABLE ONLY tab_reparacion_re
    ADD CONSTRAINT tab_reparacion_re_pkey PRIMARY KEY (id_re);
ALTER TABLE ONLY tab_representante_r
    ADD CONSTRAINT tab_representante_r_pkey PRIMARY KEY (ci_r);
ALTER TABLE ONLY tab_canaima_representante_cr
    ADD CONSTRAINT tab_canaima_representante_cr_pkey PRIMARY KEY (id_cr);
ALTER TABLE ONLY tab_canaima_representante_cr
    ADD CONSTRAINT beneficio1 FOREIGN KEY (ci_r) REFERENCES tab_representante_r(ci_r) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE ONLY tab_canaima_representante_cr
    ADD CONSTRAINT beneficio2 FOREIGN KEY (serial_c) REFERENCES tab_canaima_c(serial_c) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE ONLY tab_canaima_c
    ADD CONSTRAINT manipula FOREIGN KEY (ci_n) REFERENCES tab_nino_n(ci_n) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE ONLY tab_reparacion_re
    ADD CONSTRAINT repara FOREIGN KEY (serial_c) REFERENCES tab_canaima_c(serial_c) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE ONLY tab_nino_n
    ADD CONSTRAINT representado FOREIGN KEY (ci_r) REFERENCES tab_representante_r(ci_r) ON UPDATE CASCADE ON DELETE CASCADE;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
