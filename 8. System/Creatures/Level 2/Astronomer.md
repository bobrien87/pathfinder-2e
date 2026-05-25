---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Astronomer"
level: "2"
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
    desc: "+10"
languages: "Common"
skills:
  - name: Skills
    desc: "Arcana +8, Occultism +8, Astronomy Lore +12"
abilityMods: ["+0", "+1", "+2", "+4", "+3", "+0"]
abilities_top:
  - name: "Living Sextant"
    desc: "If the astronomer is able to see the night sky, they can Sense Direction using Astronomy Lore."
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +5, **Will** +9"
health:
  - name: HP
    desc: "23"
abilities_mid:
  - name: "Reject Myth"
    desc: "`pf2:r` **Trigger** A creature within 30 feet Casts a Spell or uses an ability with the fortune or misfortune trait <br>  <br> **Effect** The astronomer's rejection of such fantasy becomes manifest. The astronomer attempts to counteract the triggering effect with a counteract modifier of +9 and a counteract rank of 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +7 (`pf2:1`) (two hand d8), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +8 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 17, attack +9<br>**1st** (4 slots) [[Alarm]], [[Gentle Landing]], [[Phantasmal Minion]], [[Sleep]]<br>**Cantrips** [[Detect Magic]], [[Read Aura]], [[Sigil]], [[Telekinetic Hand]], [[Telekinetic Projectile]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Different cultures have created stories about the hows and whys of the universe, if things exist beyond the stars, and if the gods manipulate the heavenly bodies. But astronomers aren't interested in folktales—they desire truth.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Astronomer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
