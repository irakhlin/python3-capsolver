from typing import Optional

from python3_capsolver.core.base import BaseCaptcha
from python3_capsolver.core.config import REQUEST_URL
from python3_capsolver.core.serializer import CaptchaResponseSer, WebsiteDataOptionsSer, RequestCreateTaskSer
from python3_capsolver.core.enum import MtCaptchaV3TypeEnm
from typing import Union, Optional

from python3_capsolver.core.base import BaseCaptcha

class MtCaptcha(BaseCaptcha):
    """
    The class is used to work with Capsolver MtCaptcha method.

    Args:
        api_key: Capsolver API key
        captcha_type: Captcha type name, like ``MtCaptchaTask`` and etc.
        websiteURL: Address of a webpage with Google ReCaptcha
        websiteKey: Recaptcha website key. <div class="g-recaptcha" data-sitekey="THAT_ONE"></div>
        pageAction: Widget action value. Website owner defines what user is doing on the page through this parameter.
                    Default value: ``verify``. Example: grecaptcha.execute('site_key', {action:'login_test'}).


    Examples:
        >>> MtCaptcha(api_key="CAI-1324...",
        ...         captcha_type=MtCaptchaV3TypeEnm.MtCaptchaTaskProxyLess,
        ...         websiteURL="https://www.mtcaptcha.com/#mtcaptcha-demo",
        ...         websiteKey="MTPublic-tqNCRE0GS",
        ...         proxy="198.22.3.1:10001:user:pwd"
        ...        ).captcha_handler()
        CaptchaResponseSer(errorId=False,
                           errorCode=None,
                           errorDescription=None,
                           taskId='73bdcd28-6c77-4414-8....',
                           status=<ResponseStatusEnm.Ready: 'ready'>,
                           solution={'token': 'v1(03,79a,MTPublic-tqNCRE0GS,c9...'}
                          )

        >>> MtCaptcha(api_key="CAI-1324...",
        ...         websiteURL="https://www.mtcaptcha.com/#mtcaptcha-demo",
        ...         websiteKey="MTPublic-tqNCRE0GS",
        ...         proxy="198.22.3.1:10001:user:pwd"
        ...        ).captcha_handler(isInvisible=False, userAgent='Mozilla/5.0 (pl.....')
        CaptchaResponseSer(errorId=False,
                           errorCode=None,
                           errorDescription=None,
                           taskId='73bdcd28-6c77-4414-8....',
                           status=<ResponseStatusEnm.Ready: 'ready'>,
                           solution={'token': 'v1(03,79a,MTPublic-tqNCRE0GS,c9...'}
                          )

        >>> await MtCaptcha(api_key="CAI-1324...",
        ...         websiteURL="https://www.mtcaptcha.com/#mtcaptcha-demo",
        ...         websiteKey="MTPublic-tqNCRE0GS",
        ...         proxy="198.22.3.1:10001:user:pwd"
        ...        ).aio_captcha_handler()
        CaptchaResponseSer(errorId=False,
                           errorCode=None,
                           errorDescription=None,
                           taskId='73bdcd28-6c77-4414-8....',
                           status=<ResponseStatusEnm.Ready: 'ready'>,
                           solution={'token': 'v1(03,79a,MTPublic-tqNCRE0GS,c9...'}
                          )

        >>> await MtCaptcha(api_key="CAI-1324...",
        ...         websiteURL="https://www.mtcaptcha.com/#mtcaptcha-demo",
        ...         websiteKey="MTPublic-tqNCRE0GS",
        ...         proxy="198.22.3.1:10001:user:pwd"
        ...        ).aio_captcha_handler(isInvisible=False, userAgent='Mozilla/5.0 (pl.....')
        CaptchaResponseSer(errorId=False,
                           errorCode=None,
                           errorDescription=None,
                           taskId='73bdcd28-6c77-4414-8....',
                           status=<ResponseStatusEnm.Ready: 'ready'>,
                            solution={'token': 'v1(03,79a,MTPublic-tqNCRE0GS,c9...'}
                          )

    Returns:
        CaptchaResponseSer model with full server response

    Notes:
        https://docs.capsolver.com/guide/captcha/MtCaptcha.html
    """

    def __init__(
        self,
        captcha_type: Union[MtCaptchaV3TypeEnm, str],
        websiteURL: str,
        websiteKey: str,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        if captcha_type in MtCaptchaV3TypeEnm.list():
            self.task_params = WebsiteDataOptionsSer(**locals()).dict()
        else:
            raise ValueError(
                f"""Invalid `captcha_type` parameter set for `{self.__class__.__name__}`,
                available - {MtCaptchaV3TypeEnm}"""
            )
        for key in kwargs:
            self.task_params.update({key: kwargs[key]})

    def captcha_handler(
        self
    ) -> CaptchaResponseSer:
        """
        Sync method for captcha solving

        Returns:
            CaptchaResponseSer model with full service response

        Notes:
            Check class docstring for more info
        """
        return self._processing_captcha(create_params=self.task_params)

    async def aio_captcha_handler(
        self
    ) -> CaptchaResponseSer:
        """
        Async method for captcha solving

        Returns:
            CaptchaResponseSer model with full service response

        Notes:
            Check class docstring for more info
        """
        return await self._aio_processing_captcha(create_params=self.task_params)
