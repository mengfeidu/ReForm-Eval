import yaml

def get_iiit5k(args, config, formulation, preprocessor):
    if config is None:
        from .ocr_dataset import OCR_SingleChoice, OCR_TrueOrFalse
        if formulation == 'SingleChoice': # but use true or false
            return OCR_SingleChoice(args=args, proc=preprocessor, duplication=args.dataset_duplication)
        elif formulation == 'TrueOrFalse':
            return OCR_TrueOrFalse(args=args, proc=preprocessor, duplication=args.dataset_duplication)
    else:
        config = yaml.load(open(config, 'r'), Loader=yaml.Loader)
        if config['task'] == 'ocr':
            from .ocr_dataset import OCR_SingleChoice,OCR_TrueOrFalse, OCR_OpenEnded
            if formulation == 'SingleChoice': # but use true or false
                return OCR_SingleChoice(args=args, proc=preprocessor, duplication=args.dataset_duplication)
            elif formulation == 'TrueOrFalse':
                return OCR_TrueOrFalse(args=args, proc=preprocessor, duplication=args.dataset_duplication)
            elif formulation == 'OCROpenEnded' or formulation == 'OpenEnded':
                return OCR_OpenEnded(args=args, proc=preprocessor, duplication=args.dataset_duplication)
            else:
                raise ValueError('current formulation {} is not supported yet'.format(formulation))