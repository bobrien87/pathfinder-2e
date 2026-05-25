---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Departmental Chair"
level: "7"
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
    desc: "+16"
languages: "Common (up to 4 additional languages)"
skills:
  - name: Skills
    desc: "Arcana +22, Diplomacy +15, Occultism +22, Society +17, Academia Lore +25, One Additional Lore +22"
abilityMods: ["+0", "+1", "+0", "+5", "+5", "+3"]
abilities_top:
  - name: "Veteran Researcher"
    desc: "On the rare occasions the departmental chair still deals with their research, they are a 10th-level challenge."
armorclass:
  - name: AC
    desc: "24; **Fort** +13, **Ref** +14, **Will** +18"
health:
  - name: HP
    desc: "115"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +13 (`pf2:1`) (magical, two hand d8), **Damage** 1d4+6 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 25, attack +17<br>**4th** (2 slots) [[Mountain Resilience]], [[Wall of Fire]]<br>**3rd** (4 slots) [[Fireball]], [[Fireball]], [[Haste]], [[Lightning Bolt]]<br>**Cantrips** [[Detect Magic]], [[Ignition]], [[Prestidigitation]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Paper Pusher"
    desc: "`pf2:1` The departmental chair has spent so much time dealing with bureaucracy recently that papers and forms have worked their way into the chair's spellcasting. If the departmental chair's next action is to Cast a Spell that deals energy damage, the spell conjures a burst of sharp-edged paper instead. Change the damage type to slashing, and the spell deals an additional 1d6 persistent bleed damage."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

All the departmental chair really wants is a chance to quietly do their research. Instead, they've been roped into dealing with every emergency—political, supernatural, or emotional—in the university. They are not thrilled about this.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Departmental Chair"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
