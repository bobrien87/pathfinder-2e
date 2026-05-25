---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Narrik"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]], [[Scent]] (imprecise) 120 feet"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Athletics +17, Intimidation +17, Stealth +15, Survival +15"
abilityMods: ["+6", "+4", "+2", "-1", "+4", "+2"]
abilities_top:
  - name: "Taste Fear"
    desc: "A narrik viscerally tastes fear. They can use scent as a precise sense when detecting frightened creatures."
  - name: "Vestigial Eyes"
    desc: "A narrik's vision is limited. It's only a precise sense within 30 feet, and an imprecise sense beyond that."
  - name: "Psychotropic Saliva"
    desc: "The target's frightened value doesn't automatically decrease at the end of its turn while affected by this poison <br>  <br> **Saving Throw** DC 22 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Frightened]] 1 (1 round) <br>  <br> **Stage 2** 1d8 poison damage and [[Frightened]] 2 (1 round) <br>  <br> **Stage 3** 1d10 poison damage and [[Frightened]] 3 (1 round)"
  - name: "Tanglespit"
    desc: "A creature hit by the narrik's tanglespit is [[Immobilized]] as the viscous glob quickly solidifies. The DC to [[Escape]] or [[Force Open]] the tanglespit is 25. The glob becomes fragile and brittle after 1 minute, automatically freeing the creature."
armorclass:
  - name: AC
    desc: "24; **Fort** +18, **Ref** +15, **Will** +12"
health:
  - name: HP
    desc: "130; **Immunities** precision"
abilities_mid:
  - name: "Catalyzing Demise"
    desc: "**Trigger** The narrik is reduced to 0 Hit Points <br>  <br> **Effect** When a narrik is slain, their internal chemistry undergoes a violent chain reaction. They explode, and all creatures in a @Template[type:emanation|distance:5] must succeed at a DC 25 [[Reflex]] save or be [[Immobilized]] by tanglespit and exposed to psychotropic saliva."
  - name: "Quick Congeal"
    desc: "A narrik's strange body chemistry causes their blood to congeal almost instantly. They automatically succeeds at flat checks to recover from persistent bleed damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`), **Damage** 2d6+8 piercing plus [[Psychotropic Saliva]]"
  - name: "Melee strike"
    desc: "Claws +18 (`pf2:1`) (agile), **Damage** 2d4+8 slashing"
  - name: "Ranged strike"
    desc: "Spit +16 (`pf2:1`) (range 30 ft.), **Damage**  plus [[Psychotropic Saliva]] plus [[Tanglespit]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Far below the surface of Golarion, packs of narriks hunt in Darklands tunnels, looking for unfortunate beings to devour. These horrific creatures are vaguely humanoid but lack a traditional head—dozens of largely vestigial eyes top their bodies, while a massive, fang-filled mouth splits their chest. Their long tongue contains olfactory organs, which narriks primarily use to hunt.

Narriks' favorite prey are sentient beings—calignis, hryngars, umbral gnomes, and surface adventurers and traders—and they savor the flavor fear adds to raw flesh. Among the assorted alchemical substances naturally produced by their bodies is a psychotropic saliva that fills victims with terror, not only enhancing the taste but also allowing narriks to more easily hunt.

Narriks have little in the way of a civilization, as they primarily spend their time hunting rather than building or other activities. Scholars are unsure how they reproduce, as none have gotten close enough to study such habits. However, there are records of attacks from markedly less mature narriks throughout history. Such assaults have occurred far from other narriks, so many believe that narrik offspring are forced to create their own packs once they reach adulthood.

```statblock
creature: "Narrik"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
