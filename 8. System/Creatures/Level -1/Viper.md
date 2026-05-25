---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Viper"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +1, Stealth +5, Survival +3"
abilityMods: ["-3", "+4", "+0", "-4", "+1", "-2"]
abilities_top:
  - name: "Viper Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 4 rounds <br>  <br> **Stage 1** 1d8 poison (1 round)."
armorclass:
  - name: AC
    desc: "14; **Fort** +2, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "8"
abilities_mid:
  - name: "Slink"
    desc: "`pf2:r` **Trigger** A creature ends its movement adjacent to the viper or within the viper's space. <br>  <br> **Effect** The viper Strides, Climbs, or Swims up to 10 feet (or up to the relevant Speed, if that Speed is less than 10 feet). It must end its movement in a location that isn't within 5 feet of a foe. This movement doesn't trigger reactions."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +6 (`pf2:1`) (agile, finesse, reach 0 ft.), **Damage** 1d8-3 piercing plus [[Viper Venom]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Each member of this family of venomous snakes has long, hinged fangs that inject potent venom into their prey. Different vipers inject different types of venom, which might result in paralysis, extreme pain and swelling, blood clotting, or even the sudden stopping of the victim's heart.

Snakes come in an array of forms, from jungle-dwelling constrictors that wrap around their prey to venomous vipers with deadly bites. Regardless, all snakes consume their prey whole by unhinging their jaws and using powerful muscles to move the food down their throats and into their stomachs.

```statblock
creature: "Viper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
