\connect wallabydb

-- Kinematic model catalogue
CREATE TABLE wallaby.kinematic_model (
  "id" BIGSERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "ra" double precision NOT NULL,
  "dec" double precision NOT NULL,
  "freq" double precision NOT NULL,
  "team_release" varchar NOT NULL,
  "team_release_kin" varchar NOT NULL,
  "vsys_model" double precision NOT NULL,
  "e_vsys_model" double precision NOT NULL,
  "x_model" double precision NOT NULL,
  "e_x_model" double precision NOT NULL,
  "y_model" double precision NOT NULL,
  "e_y_model" double precision NOT NULL,
  "ra_model" double precision NOT NULL,
  "e_ra_model" double precision NOT NULL,
  "dec_model" double precision NOT NULL,
  "e_dec_model" double precision NOT NULL,
  "inc_model" double precision NOT NULL,
  "e_inc_model" double precision NOT NULL,
  "pa_model" double precision NOT NULL,
  "e_pa_model" double precision NOT NULL,
  "pa_model_g" double precision NOT NULL,
  "e_pa_model_g" double precision NOT NULL,
  "qflag_model" integer NOT NULL,
  "rad" varchar NOT NULL,
  "vrot_model" varchar NOT NULL,
  "e_vrot_model" varchar NOT NULL,
  "e_vrot_model_inc" varchar NOT NULL,
  "rad_sd" varchar NOT NULL,
  "sd_model" varchar NOT NULL,
  "sd_fo_model" varchar NOT NULL,
  "e_sd_model" varchar NULL,
  "e_sd_fo_model_inc" varchar NULL,
  "r_hi" double precision NULL,
  "v_disp" double precision NULL,
  "v_rhi" double precision NULL,
  "kinver" varchar NOT NULL,
);
ALTER TABLE wallaby.kinematic_model ADD FOREIGN KEY ("name") REFERENCES wallaby.source ("name") ON DELETE CASCADE;


-- Kinematic model product files
CREATE TABLE wallaby.wkapp_product (
  "id" BIGSERIAL PRIMARY KEY
);
ALTER TABLE wallaby.wkapp_product ADD COLUMN "kinematic_model_id" BIGINT NOT NULL;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "baroloinput" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "barolomod" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "barolosurfdens" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "diagnosticplot" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "diffcube" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "fatinput" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "fatmod" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "fullresmodcube" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "fullresproccube" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "modcube" bytea;
ALTER TABLE wallaby.wkapp_product ADD COLUMN "procdata" bytea;
ALTER TABLE wallaby.wkapp_product ADD FOREIGN KEY ("kinematic_model_id") REFERENCES wallaby.kinematic_model ("id") ON DELETE CASCADE;


CREATE TABLE wallaby.wrkp_product (
  "id" BIGSERIAL PRIMARY KEY
);
