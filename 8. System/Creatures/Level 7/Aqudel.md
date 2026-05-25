---
type: creature
group: ["Aberration", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aqudel"
level: "7"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Aklo, Alghollthu, Common, Sakvroth, Thalassic (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +17, Deception +15, Intimidation +17, Occultism +18, Stealth +15, Lore (any one subcategory) +16"
abilityMods: ["+6", "+2", "+5", "+5", "+3", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24 all-around vision; **Fort** +18, **Ref** +11, **Will** +16"
health:
  - name: HP
    desc: "120"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +16 (`pf2:1`) (reach 20 ft.), **Damage** 2d10+9 bludgeoning"
  - name: "Melee strike"
    desc: "Cirrus +16 (`pf2:1`) (agile, versatile p), **Damage** 2d8+6 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 26, attack +17<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Suggestion]]<br>**3rd** [[Mind Reading]] (At Will)<br>**2nd** [[Telekinetic Maneuver]] (At Will)<br>**1st** [[Charm]]"
abilities_bot:
  - name: "Barbed Cirri"
    desc: "`pf2:2` The aqudel makes up to four cirrus Strikes, each against a diferent target. These attacks count toward the aqudel's multiple attack penalty, but the multiple attack penalty doesn't increase until after they makes all of their attacks."
  - name: "Strobe"
    desc: "`pf2:2` The aqudel changes the intensity and pattern of their skin in a rapid pulse, attempting to disorient any creatures that can see them. Creatures within 30 feet of the aqudel must attempt a DC 25 [[Will]] save. The aqudel can't use Strobe again for 1d4 rounds. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is [[Dazzled]] for 1 round. <br> - **Failure** The target is dazzled for 1 minute and [[Stunned]] 1. <br> - **Critical Failure** The target is dazzled for 1 minute and [[Stunned]] 2"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Aqudels are obsessed with control. They consider everything around them open to manipulation, and their position in the alghollthu hierarchy leads them to lord over networks of ugothols or small, established societies that they often bully and exploit from the shadows. Aqudels answer only to vidileths, following their commands with a combination of simpering compliance and scheming distrust.

```statblock
creature: "Aqudel"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
