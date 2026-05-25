---
type: creature
group: ["Fey", "Gremlin"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jinkin"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: "Gremlin"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +7, Crafting +5, Deception +5, Nature +5, Stealth +7, Thievery +7"
abilityMods: ["-2", "+4", "+0", "+2", "+2", "+2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The jinkin deals 1d6 extra precision damage to [[Off Guard]] creatures."
  - name: "Tinker"
    desc: "A group of six jinkins can work together for an hour to imbue an item with a curse at a range of 60 feet. While this process is lengthy, it's also unobtrusive and can be performed while [[Hiding]]. Jinkins prefer to use this ability on magic items. The curse makes the item unreliable (DC 5 flat check or waste any action to Interact with or Activate the item), adds a bizarre requirement to use the item, or imparts some other curse of a similar caliber."
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "19; **Weaknesses** cold iron 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +9 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 1d6-2 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17, attack +9<br>**1st** [[Prestidigitation]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Jinkins are sadistic tinkers who steal and sabotage items and take great pride in their power to curse precious objects. They hold grudges and create convoluted plans for revenge when they feel slighted, such as when a creature dares to remove one of their curses. Rarely content to wreak simple mayhem, jinkins also take immense pleasure in torture and murder, though they prefer to lead victims into traps designed to capture or incapacitate rather than just kill them outright. Deep pits are a preferred method, since victims who survive their fall face a slow death from starvation and thirst while jinkins gather at the edge of pits to tease and torment them.

Gremlins are cruel fey tricksters and saboteurs who have fully acclimated to life in the Universe, finding distinct niches for their inventive destructiveness. Nearly all gremlins delight in ruining or breaking things, whether it's something physical like a device or vehicle or something intangible such as an alliance or relationship. A gremlin's greatest joy is watching the collapse of complex creations, preferably after the slightest, carefully targeted nudge from the gremlin. Gremlins tend to denigrate, bully, or even slaughter their lesser kin, particularly mitflits, whom stronger gremlins derisively call "baggies."

```statblock
creature: "Jinkin"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
