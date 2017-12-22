import ena_types
import argparse
import ConfigParser



def main(outputDir, conf_path):
    config = ConfigParser.ConfigParser()
    config.readfp(open(conf_path))

    number_config = config.getint('CommunityDesign', 'number_of_samples')
    sample = ena_types.Sample()

    study = ena_types.Study()
    study.center_project_name = "CAMI"
    study.study_description = "Benchmarking Contest"
    study.study_title = "CAMI - Critical Assessment of Metagenome Interpretation"

    experiment = ena_types.Experiment(study)
    run = ena_types.Run(experiment)

    for x in range(0, number_config):
        run.add_file("samplefile1")

    run.build()
    ena_types.output(outputDir, sample.build(), study.get_ena_type(), experiment.build(), run.get_ena_type())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-out",
        help="Output directory")
    parser.add_argument(
        "-conf",
        help="Config file")
    options = parser.parse_args()
    outputDir = options.out
    config = options.conf
    main(outputDir, config)