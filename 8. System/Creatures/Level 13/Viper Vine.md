---
type: creature
group: ["Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Viper Vine"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Plant"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Low-Light Vision]], [[Tremorsense]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +27, Stealth +24"
abilityMods: ["+8", "+5", "+7", "-4", "+5", "-3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "33; **Fort** +26, **Ref** +24, **Will** +22"
health:
  - name: HP
    desc: "270; **Resistances** poison 15"
abilities_mid:
  - name: "Cold Vulnerability"
    desc: "When exposed to a cold effect, the viper vine is overwhelmed by lethargy, becoming [[Slowed]] 1 for 1d4 rounds."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +27 (`pf2:1`) (reach 10 ft.), **Damage** 3d6+11 piercing plus 3d6 poison"
  - name: "Melee strike"
    desc: "Vine +25 (`pf2:1`) (agile, reach 15 ft.), **Damage** 3d10+11 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Captivating Pollen"
    desc: "`pf2:1` The viper vine releases a @Template[type:emanation|distance:60] of [[Invisible]] pollen that stays in the air for 5 rounds unless dispersed by a moderate or stronger wind. Each creature that enters or starts its turn in the area must succeed at a DC 33 [[Will]] save or be captivated. The viper vine can't use Captivating Pollen for 1d4 rounds. <br> - **Critical Success** The creature is unaffected and is temporarily immune to Captivating Pollen for 24 hours. <br> - **Success** The creature is [[Sickened]] 1. <br> - **Failure** The creature is [[Fascinated]], and it must spend each of its actions to move closer to the viper vine as expediently as possible while avoiding obvious dangers. If a captivated creature is adjacent to the viper vine, it stays still and doesn't act. It ceases to be fascinated if it's no longer in the pollen aura at the end of its turn. <br> - **Critical Failure** As failure, plus the creature is [[Stupefied 2]] for 24 hours."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(3d8+8)[bludgeoning]] damage, DC 33 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A voracious, flesh-eating carnivore, the viper vine has a single enormous blossom arising from a thick, leafy tangle of snakelike vines. When the plant senses the approach of suitable prey through its sensitive, shallow-buried root system, it rises up like an agitated snake and unfurls its brightly colored bloom, an act that releases a cloud of mind-numbing pollen.

Since viper vines gain nourishment by consuming creatures rather than through photosynthesis and absorbing nutrients from the soil, they have developed rudimentary locomotion and can drag themselves along the ground with tentacle-like roots. They even have a form of rudimentary sentience, allowing them to both discern differences in prey and make limited tactical decisions, while also avoiding creatures that are particularly large or dangerous looking.

The area around viper vine hunting grounds is often strewn with the partially devoured remains of victims. It's not unusual to find the rotting corpses of wild animals, ill-fated adventurers, and even giants in the plant's immediate vicinity, along with a scattering of incidental treasure left behind on the corpses. A viper vine rarely returns to the carcass of a creature it killed earlier, preferring to hunt fresh meat.

```statblock
creature: "Viper Vine"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
