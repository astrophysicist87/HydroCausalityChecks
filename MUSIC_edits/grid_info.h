// Copyright 2012 Bjoern Schenke, Sangyong Jeon, and Charles Gale
// Copyright 2014-2016 Chun Shen
#ifndef SRC_GRID_INFO_H_
#define SRC_GRID_INFO_H_

#include <iostream>
#include <iomanip>
#include <string>

#include "data.h"
#include "eos.h"
#include "cell.h"
#include "grid.h"
#include "pretty_ostream.h"
#include "transport_coeffs.h"
#include "HydroinfoMUSIC.h"

class Cell_info {
 private:
    const InitData &DATA;
    const EOS &eos;
    TransportCoeffs transport_coeffs_;

    pretty_ostream music_message;
    
    int deltaf_qmu_coeff_table_length_T;
    int deltaf_qmu_coeff_table_length_mu;
    double delta_qmu_coeff_table_T0;
    double delta_qmu_coeff_table_mu0;
    double delta_qmu_coeff_table_dT;
    double delta_qmu_coeff_table_dmu;
    double **deltaf_qmu_coeff_tb;
    int deltaf_coeff_table_14mom_length_T;
    int deltaf_coeff_table_14mom_length_mu;
    double delta_coeff_table_14mom_T0;
    double delta_coeff_table_14mom_mu0;
    double delta_coeff_table_14mom_dT;
    double delta_coeff_table_14mom_dmu;
    double **deltaf_coeff_tb_14mom_DPi;
    double **deltaf_coeff_tb_14mom_BPi;
    double **deltaf_coeff_tb_14mom_BPitilde;
    double **deltaf_coeff_tb_14mom_BV;
    double **deltaf_coeff_tb_14mom_DV;
    double **deltaf_coeff_tb_14mom_Bpi_shear;

 public:
    Cell_info(const InitData &DATA_in, const EOS &eos_ptr_in);
    ~Cell_info();

    //! This function outputs a header files for JF and Gojko's EM programs
    void Output_hydro_information_header();

    //! This function outputs hydro evolution file
    void OutputEvolutionDataXYEta(SCGrid &arena, double tau);

    //! This function outputs hydro evolution file into memory for JETSCAPE
    void OutputEvolutionDataXYEta_memory(
                SCGrid &arena, double tau, HydroinfoMUSIC &hydro_info_ptr);

    //! This function outputs hydro evolution file in binary format
    void OutputEvolutionDataXYEta_chun(SCGrid &arena, double tau);

	//! This function outputs hydro information needed to evaluate causality conditions
	void OutputEvolutionDataXYEta_CPlumberg(SCGrid &arena, double tau);

    //! This function outputs hydro evolution file in binary format for photon production
    void OutputEvolutionDataXYEta_photon(SCGrid &arena, double tau);

    void load_deltaf_qmu_coeff_table(std::string filename);
    void load_deltaf_qmu_coeff_table_14mom(std::string filename);
    double get_deltaf_qmu_coeff(double T, double muB);
    double get_deltaf_coeff_14moments(double T, double muB, double type);


    //! This function computes the inverse Reynolds number for a given fluid
    //! cell at (ix, iy, ieta)
    void calculate_inverse_Reynolds_numbers(
                        SCGrid &arena_current,
                        const int ieta, const int ix, const int iy,
                        double &R_pi, double &R_Pi) const;
    
    void OutputEvolution_Knudsen_Reynoldsnumbers(SCGrid &arena,
                                                 double tau) const;

    //! This function outputs files to check with Gubser flow solution
    void Gubser_flow_check_file(SCGrid &arena, double tau);

    //! This function outputs files to cross check with 1+1D simulation
    void output_1p1D_check_file(SCGrid &arena, double tau);

    //! This function prints to the screen the maximum local energy density,
    //! the maximum temperature in the current grid
    double get_maximum_energy_density(SCGrid &arena);

    //! This function outputs energy density and n_b for making movies
    void output_evolution_for_movie(SCGrid &arena, double tau);

    //! This function outputs average T and mu_B as a function of proper tau
    //! within a given space-time rapidity range
    void output_average_phase_diagram_trajectory(
                double tau, double eta_min, double eta_max, SCGrid &arena);

    //! This function dumps the energy density and net baryon density
    void output_energy_density_and_rhob_disitrubtion(SCGrid &arena,
                                                     std::string filename);
    
    //! This function checks the total energy and total net baryon number
    //! at a give proper time
    void check_conservation_law(SCGrid &arena, SCGrid &arena_prev, double tau);

    //! This function outputs the evolution of hydrodynamic variables at a
    //! give fluid cell
    void monitor_fluid_cell(SCGrid &arena, int ix, int iy, int ieta,
                            double tau);

    //! This function outputs system's momentum anisotropy as a function of tau
    void output_momentum_anisotropy_vs_tau(
                double tau, double eta_min, double eta_max, SCGrid &arena);
};

#endif  // SRC_GRID_INFO_H_
