Economics
=========

This section provides a general discussion of the generalized Roy model and selected issues in the econometrics of policy evaluation.

Generalized Roy Model
---------------------

The generalized Roy model (:cite:`Roy1951`, :cite:`HecVyr05`) provides a coherent framework to  explore the econometrics of policy evaluation. Its is characterized by the following set of equations.

.. math::
    :nowrap:

    \begin{align*}
    & \textbf{Potential Outcomes} & &  \\
    & & Y_1 & = \mu_1(X) + U_1 \\
    & & Y_0 & = \mu_0(X) + U_0 \\
    & & & \\
    & \textbf{Choice} & &  \\
    & & C & = \mu_C(Z) - V \\
    & & D & = I[C  > 0 ] \\
    & & S & = E[Y_1 - Y_0 \mid \mathcal{I}] \\
    & & & \\
    & \textbf{Observed Outcome} & &  \\
    & & Y & = D Y_1 + (1 - D) Y_0
    \end{align*}

:math:`(Y_1, Y_0)` are objective outcomes associated with each potential treatment state :math:`D` and realized after the treatment decision. :math:`Y_1` refers to the outcome in the treated state and :math:`Y_0` in the untreated state. :math:`C` denotes the propensity for treatment participation. Any subjective benefits, e.g. job amenities, and costs, e.g. tuition costs, are included in the subjective propensity of treatment. Agents take up treatment :math:`D` if their propensity :math:`C` is positive. I denotes the agent’s information set at the time of the participation decision. The observed outcome :math:`Y` is determined in a switching-regime fashion (:cite:`Quandt1958`, :cite:`Quandt1972`). If agents take up treatment, then the observed outcome :math:`Y` corresponds to the outcome in the presence of treatment :math:`Y_1`. Otherwise, :math:`Y_0` is observed. The unobserved potential outcome is referred to as the counterfactual outcome. If costs are identically zero for all agents, there are no observed regressors, and :math:`(U_1, U_0) \sim N (0, \Sigma)`, then the generalized Roy model corresponds to the original
Roy model (:cite:`Roy1951`).

From the perspective of the econometrician, :math:`(X, Z)` are observable while :math:`(U_1, U_0, V)` are not. :math:`X` are the observed determinants of potential outcomes :math:`(Y_1, Y_0)`, and :math:`Z` are the observed determinants of the cost of treatment :math:`C`. Potential outcomes and cost are decomposed into their means :math:`(\mu_1(X), \mu_0(X), \mu_C(Z))` and their deviations from the mean :math:`(U_1, U_0, V)`. :math:`(X, Z)` might have common elements. Observables and unobservables jointly determine program participation :math:`D`.

If their ex ante surplus :math:`S` from participation is positive, then agents select into treatment. Yet, this does not require their expected objective returns to be positive as well. Subjective cost :math:`C` might be negative such that agents which expect negative returns still participate. Moreover, in the case of imperfect information, an agent’s ex ante evaluation of treatment is potentially different from their ex post assessment.

The evaluation problem arises because either :math:`Y_1` or :math:`Y_0` is observed. Thus, the effect of treatment cannot be determined on an individual level. If the treatment choice :math:`D` depends on the potential outcomes, then there is also a selection problem. If that is the case, then the treated and untreated differ not only in their treatment status but in other characteristics as well. A naive comparison of the treated and untreated leads to misleading conclusions. Jointly, the evaluation and selection problem are the two fundamental problems of causal inference (:cite:`Holland86`).

Selected Issues
---------------
Using the setup of the generalized Roy model, we now highlight several important concepts in the economics and econometrics of policy evaluation. We discuss sources of agent heterogeneity and motivate alternative objects of interest.

Agent Heterogeneity
^^^^^^^^^^^^^^^^^^^^

What gives rise to variation in choices and outcomes among, from the econometrician’s perspective, otherwise observationally identical agents? This is the central question in all econometric policy analyses (:cite:`BrHecHa07`, :cite:`Heckman2001`).

The individual benefit of treatment is defined as

  .. math::
       B  = Y_1 - Y_0 = (\mu_1(X) - \mu_0(X)) + (U_1 - U_0).

From the perspective of the econometrician, differences in benefits are the result of variation in observable X and unobservable characteristics :math:`(U_1 - U_0)`. However, :math:`(U_1 - U_0)` might be (at least partly) included in the agent’s information set I and thus known to the agent at the time of the treatment decision.

As a result, unobservable treatment effect heterogeneity can be distinguished into private information and uncertainty. Private information is only known to the agent but not the econometrician; uncertainty refers to variability that is unpredictable by both.

The information available to the econometrician and the agent determines the set of valid estimation approaches for the evaluation of a policy. The concept of essential heterogeneity emphasizes this point (:cite:`HeUrVy06`).

Essential Heterogeneity
^^^^^^^^^^^^^^^^^^^^^^^^

If agents select their treatment status based on benefits unobserved by the econometrician (selection on unobservables), then there is no unique effect of a treatment or a policy even after conditioning on observable characteristics. Average benefits are different from marginal benefits, and different policies select individuals at different margins. Conventional econometric methods that only account for selection on observables, like matching (:cite:`CocRub72`, :cite:`RoRu1983`, :cite:`HeIcSmTo98`), are not able to identify any parameter of interest (:cite:`HecVyr05`, :cite:`HeUrVy06`). For example, Carneiro (2011) (:cite:`Carneiro2011`) present evidence on agents selecting their level of education based on their unobservable gains and demonstrate the importance of adjusting the estimation strategy to allow for this fact. Heckman and Schmierer (:cite:`Heckman2010`) propose a variety of tests for the the presence of essential heterogeneity.

.. todo::

    Set up proper citations.

Objects of Interest
-------------------

Treatment effect heterogeneity requires to be precise about the effect being discussed. There is no single effect of neither a policy nor a treatment. For each specific policy question, the object of interest must be carefully defined (:cite:`HecVyr05`, :cite:`HecVyr07a`, :cite:`HecVyr07b`). We present several potential objects of interest and discuss what question they are suited to answer. We start with the average effect parameters. However, these neglect possible effect heterogeneity. Therefore, we explore their distributional counterparts as well.

Conventional Average Treatment Effects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is common to summarize the average benefits of treatment for different subsets of the population. In general, the focus is on the average effect in the whole population, the average treatment effect :math:`\left(B^{ATE}\right)`, or the average effect on the
treated :math:`\left(B^{TT}\right)` or untreated :math:`\left(B^{TUT}\right)`.

  .. math::
       B^{ATE} & = E [Y_1 - Y_0]\\
       B^{TT} & = E [Y_1 - Y_0 | D = 1]\\
       B^{TUT} & = E [Y_1 - Y_0 | D = 0]\\

All average effect parameter possibly hide considerable treatment effect heterogeneity. The relationship between these parameters depends on the assignment mechanism that matches agents to treatment. If agents select their treatment status based on their own benefits, then agents that take up treatment benefit more than those that do not and thus :math:`B^{TT}` > :math:`B^{ATE}`. If agents select their treatment status at random, then all parameters are equal.

.. figure:: ../docs/figures/fig-treatment-effects-with-and-without-eh.png
   :align: center

   Conventional treatment effects with and without essential heterogeneity



The policy relevance of the conventional treatment effect parameters is limited. They are only informative about extreme policy alternatives. The :math:`B^{ATE}` is of interest to policy makers if they weigh the possibility of moving a full economy from a baseline to an alternative state or are able to assign agents to treatment at random. The :math:`B^{TT}` is informative if the complete elimination of a program already in place is considered. Conversely, if the same program is examined for
compulsory participation, then the TUT is the policy relevant parameter.


To ensure a tight link between the posed policy question and the parameter of interest, Heckman
and Vytlacil (:cite:`HecVyr01`) propose the policy-relevant treatment effect :math:`\left(B^{PRTE}\right)`. They consider policies that do not change potential outcomes, but only affect individual choices. Thus, they account for voluntary program participation.

Policy-Relevant Average Treatment Effect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Policy-Relevant Average Treatment Effects The :math:`B^{PRTE}` captures the average change in outcomes per net person shifted by a change from a baseline state :math:`B` to an alternative policy :math:`A`. Let :math:`D_B` and :math:`D_A` denote the choice taken under the baseline and the alternative policy regime
respectively. Then, observed outcomes are determined as

.. math::
    Y_B & = D_BY_1 + (1 - D_B)Y_0\\
    Y_A & = D_AY_1 + (1 - D_A)Y_0.

A policy change induces some agents to change their treatment status :math:`\left(D_B \neq D_A\right)`:, while others are unaffected. More formally, the :math:`B^{PRTE}` is then defined as

.. math::
      B^{PRTE}  = E[D_A] - E[D_B](E[Y_A] - E[Y_B]).

In our empirical illustration, in which we consider education policies, the lack of policy relevance of the conventional effect parameters is particularly evident. Rather than directly assigning individuals a certain level of education, policy makers can only indirectly affect schooling choices, e.g. by altering tuition cost through subsidies. The individuals drawn into treatment by such a policy will neither be a random sample of the whole population, nor the whole population of
the previously (un-)treated.

Local Average Treatment Effect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Local Average Treatment Effect :math:`\left(B^{LATE}\right)` was introduced by Imbens and Angrist (:cite:`Imbens94`). They show that instrumental variable estimator identify :math:`B^{LATE}`, which measures the mean gross return to treatment for individuals induced into treatment by a change in an instrument.

.. figure:: ../docs/figures/fig-local-average-treatment.png
   :align: center

   :math:`B^{LATE}` at different values of :math:`u_S`

Unfortunately, the people induced to go into state 1 :math:`(D=1)` by a change in any particular instrument need not to be the same as the people induced to to go to state 1 by policy changes other than those corresponding exactly to the variation in the instrument. A desired policy effect may bot be directly correspond to the variation in the IV. Moreover, if there is a vector of instruments that generates choice and the components of the vector are intercorrelated, IV estimates using the components of :math:`Z` as the instruments, one at a time, do not, in general, identify the policy effect corresponding to varying that instruments, keeping all other instruments fixed, the ceteris paribus effect of the change in the instrument. Heckman develops this argument in detail (:cite:`Heckman10`).

The average effect of a policy and the average effect of a treatment are linked by the marginal treatment effect :math:`\left(B^{MTE}\right)`. The :math:`B^{MTE}` was introduced into the literature by Björklund and Moffitt (:cite:`BjöMof87`) and extended by Heckman and Vytlacil (:cite:`HecVyr01`, :cite:`HecVyr05`, :cite:`HecVyr07b`).

Marginal Treatment Effect
^^^^^^^^^^^^^^^^^^^^^^^^^^

The :math:`B^{MTE}` is the treatment effect parameter that conditions on the unobserved desire to select into treatment. Let :math:`V` be the heterogeneity/error effect that impacts the propensity for treatment and let :math:`U_S = F_V (V)`. Then, the :math:`B^{MTE}` is defined as

.. math::
      B^{MTE}(x, u_S)  = E [ Y_1 - Y_0 | X = x, U_S = u_S] .

The :math:`B^{MTE}` is the average benefit for persons with observable characteristics :math:`X = x` and unobservables :math:`U_S = u_S`. By construction, :math:`U_S` denotes the different quantiles of :math:`V` . So, when varying :math:`U_S` but keeping :math:`X` fixed, then the :math:`B^{MTE}` shows how the average benefit varies along the distribution of :math:`V` . For :math:`u_S` evaluation points close to zero, the :math:`B^{MTE}` is the average effect of treatment for individuals with a value of :math:`V` that makes them most likely to participate. The opposite is true for high values of :math:`u_S`.
The :math:`B^{MTE}` provides the underlying structure for all average effect parameters previously discussed. These can be derived as weighted averages of the :math:`B^{MTE}` (:cite:`HecVyr05`).

Parameter :math:`j, \Delta j (x)`, can be written as

.. math::
    \Delta j (x) = \int_{0}^{1} MTE(x, u_S) \omega^{j}(x, u_S) du_S,


where the weights :math:`\omega^{j} (x, u_S)` are specific to parameter j, integrate to one, and can be constructed from data.

.. figure:: ../docs/figures/fig-weights-marginal-effect.png
   :align: center

   Weights for the marginal treatment effect for different parameters.

All parameters are identical only in the absence of essential heterogeneity. Then, the :math:`B^{MTE}(x, u_S)` is constant across the whole distribution of :math:`V` as agents do not select their treatment status based on their unobservable benefits.

.. figure:: ../docs/figures/fig-eh-marginal-effect.png
   :align: center

   :math:`B^{MTE}` in the presence and absence of essential heterogeneity.



So far, we have only discussed average effect parameters. However, these conceal possible treatment effect heterogeneity, which provides important information about a treatment. Hence, we now present their distributional counterparts (:cite:`AaHeVy2005`).


Distribution of Potential Outcomes
-----------------------------------

Several interesting aspects of policies cannot be evaluated without knowing the joint distribution of potential outcomes (see :cite:`AbbHec07` and :cite:`HeSmCl97`). The joint distribution of :math:`(Y_1, Y_0)` allows to calculate the whole distribution of benefits. Based on it, the average treatment and policy effects can be
constructed just as the median and all other quantiles. In addition, the portion of people that benefit from treatment can be calculated for the overall population :math:`Pr(Y_1 - Y_0 > 0)` or among any subgroup of particular interest to policy makers :math:`Pr(Y_1 - Y_0 > 0 | X)`. This is important as a treatment which is beneficial for agents on average can still be harmful for some. For a comprehensive overview on related work see :cite:`AbbHec07` and the work they cite. The survey by :cite:`Fortin2011` provides an overview about the alternative approaches to the construction of conterfactual observed outcome distributions. See :cite:`Firpo2007`, :cite:`AbAnIm2002` and :cite:`Chernozhukov2005` for their studies of quantile treatment effects.

The absence of an average effect might be the result of part of the population having a positive effect, which is just offset by a negative effect on the rest of the population. This kind of treatment effect heterogeneity is informative as it provides the starting point for an adaptive research strategy that tries to understand the driving force behind these differences (:cite:`HSMV96`, :cite:`HSMV97`).

.. figure:: ../docs/figures/fig-distribution-joint-potential.png
   :align: center

   Distribution of potential Outcomes


.. figure:: ../docs/figures/fig-distribution-joint-surplus.png
  :align: center

  Distribution of benefits and surplus


.. todo::

    * add fotnote 5 from my manuscript into text
