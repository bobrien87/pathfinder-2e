---
type: creature
group: ["Dromaar", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dromaar Lorekeeper"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dromaar"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Orc"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: "Common, Orcish"
skills:
  - name: Skills
    desc: "Diplomacy +12, Occultism +11, Performance +12, Society +13, Orc Lore +15"
abilityMods: ["+1", "+3", "+0", "+2", "+2", "+3"]
abilities_top:
  - name: "Spotlight Ready"
    desc: "When performing for crowds of 10 or more, the dromaar lorekeeper gains a +2 circumstance bonus to their Performance check."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +12, **Will** +13"
health:
  - name: HP
    desc: "70"
abilities_mid:
  - name: "Final Tale"
    desc: "When the lorekeeper dies, they utter a brief but poignant final story that shakes those nearby to their core. Each creature in a @Template[type:emanation|distance:10] must succeed at a DC 20 [[Will]] save or be [[Paralyzed]] for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +14 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+4 piercing plus 1d10 sonic"
  - name: "Melee strike"
    desc: "Dagger +15 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing plus 1d10 sonic"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning plus 1d10 sonic"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14<br>**3rd** (2 slots) [[Enthrall]], [[Heroism]]<br>**2nd** (3 slots) [[Laughing Fit]], [[Noise Blast]], [[Translate]]<br>**1st** (3 slots) [[Bless]], [[Daze]], [[Figment]], [[Message]], [[Phantasmal Minion]], [[Summon Instrument]], [[Telekinetic Projectile]], [[Ventriloquism]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Lorekeepers are meticulous keepers of the colorful and often misunderstood history of orcs and dromaar. They're jovial wanderers, telling their stories to anyone who will listen.

Orcs have a strict moral code encompassing valor and accomplishment, and they cast out those unwilling to follow it. For the last few generations, orcs have been trying to erase the narratives around their culture as being solely focused on war and violence. They invite other races and adventuring parties inside their holds so they may experience the truth of who the orcs are.

```statblock
creature: "Dromaar Lorekeeper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
