---
type: creature
group: ["Beast", "Girtablilu"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Girtablilu Sentry"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Girtablilu"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: "Common, Girtablilu"
skills:
  - name: Skills
    desc: "Athletics +18, Intimidation +17, Religion +16, Survival +17"
abilityMods: ["+6", "+4", "+6", "+3", "+4", "+3"]
abilities_top:
  - name: "Desert Passage"
    desc: "A girtablilu ignores natural difficult terrain in the desert."
  - name: "Girtablilu Venom"
    desc: "**Saving Throw** DC 24 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d6 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 3d6 poison damage and enfeebled 1 (1 round) <br>  <br> **Stage 3** 3d6 poison damage and [[Enfeebled]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "27; **Fort** +20, **Ref** +16, **Will** +12"
health:
  - name: HP
    desc: "160"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +21 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d8+9 piercing"
  - name: "Melee strike"
    desc: "Pincer +20 (`pf2:1`) (agile, unarmed), **Damage** 2d8 + 9 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Stinger +20 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d6 + 9 piercing plus [[Girtablilu Venom]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d8+6)[bludgeoning]], DC 24 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sentries patrol the outskirts of girtablilu communities, watching for external threats like desert drakes, stormcrown dragons, or adventuring parties set on recklessly exploring the girtablilus' sacred sites.

Girtablilus are desert-dwelling guardians with the upper bodies of muscular humanoids and the lower bodies of massive scorpions. They are most often found defending ancient temples and religious artifacts with zealous fervor. Some believe they were created by a long-dead god millennia ago to act as guardians, but girtablilus consider the subject of their origin taboo and refuse to address the theory.

Because girtablilus accept a wide range of religions and belief systems, some outsiders believe they also worship their own ancient pantheon. In truth, girtablilus exclusively revere and protect sites dedicated to deities considered lost to civilization. In this way, they act as preservers of holy practices that have otherwise been forgotten beneath the desert's shifting sands.

Though girtablilus are used to explorers seeking entrance to the sites they defend, they might welcome those who earnestly wish to learn or offer reverence. Some even proudly share their beliefs with others, eager for the opportunity to preach to someone new. They show no mercy, however, to those who attempt to desecrate the sites and objects of their worship, or to those who would violate the tenets of their faith.

Girtablilus are skilled fighters who keep trained giant scorpions as pets, and they remain unmatched when it comes to fighting in the desert. They require relatively little food or water, and they rely on their stamina to outlast their enemies. When necessary, they can stalk their quarry for days or even weeks, coordinating with their pets to drive their prey in circles. Once exhausted, few foes can stand up to a girtablilu's physical prowess—or to their deadly venom.

```statblock
creature: "Girtablilu Sentry"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
