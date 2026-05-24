---
statblock: true
layout: Basic Pathfinder 2e Layout
type: creature
group: ["Undead", "Spellcaster"]
name: "Lich"
level: "12"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: "Neutral Evil"
size: "Medium"
trait_01: "Undead"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; Darkvision, Senses: lifesense (imprecise) 60 feet"
languages: "Common, Draconic, Elven, Necril"
skills:
  - name: Skills
    desc: "Arcana +26, Crafting +24, Deception +22, Diplomacy +22, Intimidation +22, Stealth +20"
abilityMods: ["+0", "+4", "+0", "+6", "+4", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "31; **Fort** +17, **Ref** +21, **Will** +23 (+1 status vs. magic)"
health:
  - name: HP
    desc: "190 (negative healing, rejuvenation); **Immunities** death effects, disease, paralyzed, poison, unconscious; **Resistances** cold 10, physical 10 (except magic bludgeoning)"
abilities_mid:
  - name: "Counterspell"
    desc: "`pf2:r` **Trigger** A creature casts a spell that the lich has prepared; **Effect** The lich expends its prepared spell to counteract the triggering spell."
speed: "25 feet"
attacks:
  - name: "Melee strike"
    desc: "Hand +24 (`pf2:1`) (finesse, magical), **Damage** 4d8 void plus paralyzing touch"
  - name: "Paralyzing Touch"
    desc: "A creature damaged by the lich's hand strike must succeed at a DC 32 Fortitude save or be paralyzed for 1 round. A creature can repeat the saving throw at the end of each of its turns to end the effect."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 32, attack +24; **6th** _chain lightning_, _disintegrate_, _vampiric exsanguination_; **5th** _cloudkill_, _dominate_, _wall of ice_; **4th** _dimension door_, _fire shield_, _fly_; **3rd** _blindness_, _haste_, _vampiric touch_; **2nd** _dispel magic_, _mirror image_, _resist energy_; **1st** _fleet step_, _magic missile_, _ray of enfeeblement_; **Cantrips (6th)** _detect magic_, _mage hand_, _ray of frost_, _read aura_, _shield_"
  - name: "Drain Soul Cage"
    desc: "`pf2:0` **Frequency** once per day; **Effect** The lich draws power from its soul cage to cast one prepared spell it has already cast today without expending the slot."
abilities_bot: []
sourcebook: "Bestiary"
source-type: "Remaster"
---
### `= this.file.name`

A powerful undead wizard who achieved immortality through a soul phylactery.

```statblock
creature: "Lich"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
