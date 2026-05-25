---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Leprechaun"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +8, Deception +9, Nature +7, Performance +9, Thievery +8, Gold Lore +7"
abilityMods: ["+1", "+4", "+1", "+3", "+3", "+4"]
abilities_top:
  - name: "Leprechaun Magic"
    desc: "Leprechauns love to use their magic to beguile others, and after generations of doing so, they've developed a strong connection to such tricks. When a leprechaun uses their innate spells to deceive, trick, or humiliate a creature, the spell DC increases to 20 and the attack modifier to +12."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +11, **Will** +10"
health:
  - name: HP
    desc: "25"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +7 (`pf2:1`), **Damage** 1d6+3 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 18, attack +10<br>**2nd** [[Illusory Creature]], [[Invisibility]]<br>**1st** [[Figment]], [[Illusory Object]], [[Light]], [[Prestidigitation]], [[Runic Weapon]], [[Telekinetic Hand]], [[Telekinetic Projectile]], [[Vanishing Tracks]], [[Ventriloquism]]"
abilities_bot:
  - name: "Create Object"
    desc: "`pf2:2` **Frequency** three times per day <br>  <br> **Effect** The leprechaun produces an item out of their hat, from behind their jacket, from within a hole in a tree stump, or from any other unexpected location. This conjured item must be no more than 1 Bulk and must be made of relatively commonplace material (such as cloth, wood, stone, or even low-value metal like iron or lead). It can't rely on intricate artistry or complex moving parts, never fulfills a Cost or the like, and can't be made of precious materials or materials with a rarity of uncommon or higher. The created object is temporary and lasts for 1 hour or until the leprechaun creates a new item, whichever comes first."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Leprechauns are mostly jovial tricksters who prefer mischief over conflict. They fill their days with as much fun, wine, and food as possible. Mostly found in forested regions, leprechauns respect nature and those who protect it.

Leprechauns do not attack on sight. Rather, they engage in conversation and try to charm, cajole, or trick those they meet into doing favors for them or freely giving over a treasured item, usually in return for illusory wealth or false promises of wealth and success. These small tricksters are masters at discerning the desires of those they meet-a knack that puts them in a powerful position when bargaining for goods or favors. They aren't above turning people against each other for their own benefit but generally not to an extent that causes harm.

In most cases, a leprechaun doesn't keep a purloined possession for long. The leprechaun most often returns such stolen prizes just in time to defuse tensions, often as they point out the humor of the situation, hoping to share their amusement and mirth with the victim. In cases where a leprechaun's trick goes too far and results in an incensed victim, the leprechaun quickly flees the conflict rather than engage in combat. This willingness to return stolen goods or to flee from battles fades as leprechauns grow older. Ancient leprechauns who have lived for thousands of years often spiral into dark bitterness and increasingly use their powers and illusions to lure those who offend them or fail to appreciate a joke into danger... or even death.

```statblock
creature: "Leprechaun"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
