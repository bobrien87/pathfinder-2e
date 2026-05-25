---
type: creature
group: ["Fiend", "Shade"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shade (Netherworld)"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Shade"
trait_03: "Shadow"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Shadowtongue"
skills:
  - name: Skills
    desc: "Athletics +7, Netherworld Lore +7"
abilityMods: ["+2", "+2", "+2", "+2", "+2", "+2"]
abilities_top:
  - name: "Planar Incarnation - Netherworld (The Mutilated)"
    desc: "All shades are formed from and personify the nature of the plane on which they manifest, and their statistics are adjusted as summarized below. They also gain any trait associated with creatures from their plane. <br>  <br> **Shadow Plane (The Mutilated)** The mutilated appear as they did in their mortal lives, yet are covered in wounds or partially adorned or wrapped in chains. <br>  <br> - **Sanctification** unholy <br> - **Language** Shadowtongue <br> - **Additional Ability** immune to bleed and fear <br> - **Melee** chain +7, **Damage** 1d8+2 bludgeoning"
armorclass:
  - name: AC
    desc: "15; **Fort** +7, **Ref** +7, **Will** +7"
health:
  - name: HP
    desc: "22; **Immunities** bleed, fear effects"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Chain +7 (`pf2:1`) (unholy), **Damage** 1d8+2 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The mutilated appear as they did in their mortal lives, yet are covered in wounds or partially adorned or wrapped in chains.

When a mortal dies, their soul travels to the Boneyard in the Outer Planes where they're judged by Pharasma, the goddess of the dead. Once judged, their soul is sent on to their final reward or punishment and, in the process, transformed into a creature known as a shade. This transformation grants the soul a new body, one whose shape is determined by the prevailing philosophical forces of the plane to which they're sent. A shade's memories from their former life usually fade, reduced to a few hazy fragments akin to half-remembered dreams. Regardless of the shade's size, power, or nature in life, they're a Medium creature in their afterlife.

Existence as a shade can last for eons but isn't necessarily eternal. Deities, powerful denizens of the Great Beyond, or even the Outer Planes can further alter a shade's nature by either reducing them into raw quintessence, spiritual essence that's then used to expand a plane's physical manifestation, or by transforming them into a new form of supernatural life such as a celestial, monitor, or fiend. Should a shade die, their body breaks down in a process akin to decay, their form reverting to the elements that make up their plane. This represents the true end of a soul's journey—their life essence reuniting with the heart of the Great Beyond to be recycled into Creation's Forge, fueling the creation of new souls.

```statblock
creature: "Shade (Netherworld)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
