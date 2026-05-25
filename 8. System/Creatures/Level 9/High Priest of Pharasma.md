---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "High Priest of Pharasma"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20"
languages: "Common, Requian"
skills:
  - name: Skills
    desc: "Diplomacy +25, Intimidation +17, Medicine +18, Performance +17, Religion +26, Boneyard Lore +27"
abilityMods: ["+1", "+2", "-1", "+3", "+5", "+4"]
abilities_top:
  - name: "Religious Specialist"
    desc: "For encounters involving religious debates, church politics, and conflicts of doctrine, the high priest is a 13th-level challenge."
  - name: "Steward of the Faithful"
    desc: "30 feet. <br>  <br> Each ally in the aura who worships [[Pharasma]] gains resistance 5 to void and a +1 status bonus to Will saves, Diplomacy checks, and Medicine checks."
  - name: "Healing Hands"
    desc: "When the high priest casts [[Heal]], they roll d10s instead of d8s."
  - name: "Restorative Channel"
    desc: "The high priest can sacrifice one prepared [[Heal]] spell to instead cast [[Cleanse Affliction]], [[Clear Mind]], [[Sound Body]], or [[Sure Footing]] at the same spell rank."
armorclass:
  - name: AC
    desc: "26; **Fort** +16, **Ref** +17, **Will** +21"
health:
  - name: HP
    desc: "150"
abilities_mid:
  - name: "Unshakable Faith"
    desc: "During a religious debate, clash of church politics, or similar conflict, the high priest gains a +4 circumstance bonus to Perception check to [[Sense Motive]] and to their Perception DC against attempt to [[Lie]] to them."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +18 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 2d4+7 piercing plus 1d10 spirit"
  - name: "Melee strike"
    desc: "Dagger +17 (`pf2:1`) (agile, magical, thrown 10, versatile s), **Damage** 2d4+7 piercing plus 1d10 spirit"
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning plus 1d10 spirit"
  - name: "Ranged strike"
    desc: "Hand Crossbow +17 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+7 piercing plus 1d10 spirit"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 28, attack +20<br>**5th** (7 slots) [[Breath of Life]], [[Heal]], [[Heal]], [[Heal]], [[Heal]], [[Heal]], [[Vision of Death]]<br>**4th** (3 slots) [[Holy Light]], [[Holy Light]], [[Vital Beacon]]<br>**3rd** (3 slots) [[Fear]], [[Ghostly Weapon]], [[Heroism]]<br>**2nd** (3 slots) [[Augury]], [[Darkvision]], [[Status]]<br>**1st** (3 slots) [[Command]], [[Mindlink]], [[Spirit Link]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Message]], [[Read Aura]], [[Vitality Lash]]"
  - name: "Cleric Domain Spells"
    desc: "DC 28, attack +20<br>**4th** [[Eradicate Undeath]]<br>**1st** [[Death's Call]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

High priests are the leaders of larger churches and similar religious establishments, watching over the lower-ranking clergy and ensuring the surrounding community is taken care of. This can be a highly political position, as the leader of the faith in an area has a powerful influence over everyday citizens.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "High Priest of Pharasma"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
