--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: classe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classe (
    code character varying(5) NOT NULL,
    nom character varying(10) NOT NULL,
    niveau smallint,
    heurecours smallint
);


ALTER TABLE public.classe OWNER TO postgres;

--
-- Name: employe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employe (
    num integer
);


ALTER TABLE public.employe OWNER TO postgres;

--
-- Name: enseignant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enseignant (
    matricule character varying(20) NOT NULL,
    nom character varying(20),
    prenom character varying(20),
    datenaissance date,
    heurecourssemaines smallint,
    status character(1)
);


ALTER TABLE public.enseignant OWNER TO postgres;

--
-- Name: enseignant_matiere; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enseignant_matiere (
    idenseignant character varying(20) NOT NULL,
    idmatiere smallint NOT NULL
);


ALTER TABLE public.enseignant_matiere OWNER TO postgres;

--
-- Name: enseignant_matiere_classe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enseignant_matiere_classe (
    idenseignant character varying(20) NOT NULL,
    idmatiere smallint NOT NULL,
    idclasse character varying(5) NOT NULL,
    jour character varying(20),
    duree smallint,
    periode TIME
);


ALTER TABLE public.enseignant_matiere_classe OWNER TO postgres;

--
-- Name: matiere; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.matiere (
    id smallint NOT NULL,
    intitule character varying(20) NOT NULL
);


ALTER TABLE public.matiere OWNER TO postgres;

--
-- Data for Name: classe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.classe (code, nom, niveau, heurecours) FROM stdin;
6A	6emeA	1	\N
6B	6emeB	1	\N
5A	5emeA	2	\N
5B	5emeB	2	\N
4A	4emeA	3	\N
4B	4emeB	3	\N
3A	3emeA	4	\N
3B	3emeB	4	\N
\.


--
-- Data for Name: employe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employe (num) FROM stdin;
2
\.


--
-- Data for Name: enseignant; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enseignant (matricule, nom, prenom, datenaissance, heurecourssemaines, status) FROM stdin;
1	M.Dupont	\N	\N	\N	\N
2	Mme.Leroy	\N	\N	\N	\N
3	M.Martin	\N	\N	\N	\N
4	Mme.Durand	\N	\N	\N	\N
5	M.Petit	\N	\N	\N	\N
6	Mme.Bernard	\N	\N	\N	\N
7	M.Richard	\N	\N	\N	\N
8	Mme.Fabre	\N	\N	\N	\N
9	M.Moreau	\N	\N	\N	\N
10	Mme.Lefevre	\N	\N	\N	\N
11	M.Rolland	\N	\N	\N	\N
12	Mme.Blanc	\N	\N	\N	\N
\.


--
-- Data for Name: enseignant_matiere; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enseignant_matiere (idenseignant, idmatiere) FROM stdin;
\.


--
-- Data for Name: enseignant_matiere_classe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enseignant_matiere_classe (idenseignant, idmatiere, idclasse, jour, duree, periode) FROM stdin;
\.


--
-- Data for Name: matiere; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.matiere (id, intitule) FROM stdin;
1	Mathematiques
2	Physiques
3	Histoire
4	ECM
5	Francais
6	Anglis
7	Chimie
8	Technologie
9	EPS
10	Geographie
11	SVT
12	ArtsPlastique
\.


--
-- Name: classe classe_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classe
    ADD CONSTRAINT classe_pkey PRIMARY KEY (code);


--
-- Name: enseignant_matiere_classe enseignant_matiere_classe_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignant_matiere_classe
    ADD CONSTRAINT enseignant_matiere_classe_pkey PRIMARY KEY (idenseignant, idmatiere, idclasse);


--
-- Name: enseignant_matiere enseignant_matiere_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignant_matiere
    ADD CONSTRAINT enseignant_matiere_pkey PRIMARY KEY (idenseignant, idmatiere);


--
-- Name: enseignant enseignant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignant
    ADD CONSTRAINT enseignant_pkey PRIMARY KEY (matricule);


--
-- Name: matiere matiere_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matiere
    ADD CONSTRAINT matiere_pkey PRIMARY KEY (id);


--
-- Name: enseignant_matiere_classe fk_this_clas; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignant_matiere_classe
    ADD CONSTRAINT fk_this_clas FOREIGN KEY (idclasse) REFERENCES public.classe(code);


--
-- Name: enseignant_matiere_classe fk_this_ens; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignant_matiere_classe
    ADD CONSTRAINT fk_this_ens FOREIGN KEY (idenseignant) REFERENCES public.enseignant(matricule);


--
-- Name: enseignant_matiere fk_this_ens; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignant_matiere
    ADD CONSTRAINT fk_this_ens FOREIGN KEY (idenseignant) REFERENCES public.enseignant(matricule);


--
-- Name: enseignant_matiere_classe fk_this_mat; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignant_matiere_classe
    ADD CONSTRAINT fk_this_mat FOREIGN KEY (idmatiere) REFERENCES public.matiere(id);


--
-- Name: enseignant_matiere fk_this_mat; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignant_matiere
    ADD CONSTRAINT fk_this_mat FOREIGN KEY (idmatiere) REFERENCES public.matiere(id);


--
-- PostgreSQL database dump complete
--

