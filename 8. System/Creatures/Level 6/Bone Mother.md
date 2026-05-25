---
type: creature
group: ["Humanoid", "Ratfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bone Mother"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Ratfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Low-Light Vision]]"
languages: "Common, Requian, Sakvroth, Ysoki"
skills:
  - name: Skills
    desc: "Deception +14, Intimidation +14, Medicine +13, Occultism +16, Performance +14, Religion +13, Society +12, Fortune-Telling Lore +16"
abilityMods: ["+0", "+3", "+0", "+2", "+3", "+4"]
abilities_top:
  - name: "Swarming"
    desc: "A ysoki can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +13, **Will** +15"
health:
  - name: HP
    desc: "80"
abilities_mid:
  - name: "Rattling Bones"
    desc: "`pf2:r` **Trigger** The bone mother or another ratfolk in their square takes damage from a melee Strike <br>  <br> **Effect** Spirits from the bones emerge to deal 2d6 spirit damage to the attacker with a DC 24 [[Will]] save."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +16 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 1d4+6 piercing plus 1d10 spirit"
  - name: "Melee strike"
    desc: "Dagger +16 (`pf2:1`) (agile, magical, thrown 10, versatile s), **Damage** 1d4+6 piercing plus 1d10 spirit"
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+6 piercing plus 1d10 spirit"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 24, attack +16<br>**3rd** (4 slots) [[Enthrall]], [[Haste]], [[Paralyze]], [[Ring of Truth]]<br>**2nd** (4 slots) [[Augury]], [[Cleanse Affliction]], [[Dispel Magic]], [[Translate]]<br>**1st** (4 slots) [[Bless]], [[Command]], [[Daze]], [[Detect Magic]], [[Guidance]], [[Light]], [[Mindlink]], [[Sanctuary]], [[Telekinetic Projectile]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The bone mother—a warren's oracle—cuts an imposing figure. Bone mothers can be any gender despite the name, wearing the skull of a giant rat and covering their clothing in dangling bones. When a member of the warren dies, they gift a bone (usually a finger bone) to the oracle, who exists as both a physical repository of those who came before and a living history of their warren.

Ysoki (or, as outsiders call them, ratfolk) in their warrens have a society that is both stern and democratic, caring and ever vigilant. And at the top is a handful of intimidating and protective figures who make sure the swarm remains safe.

```statblock
creature: "Bone Mother"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
