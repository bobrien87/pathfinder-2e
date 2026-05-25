---
type: creature
group: ["Shade"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shade (Universe)"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Shade"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "any one spoken in life (such as common)"
skills:
  - name: Skills
    desc: "Athletics +7, Planar Lore +7"
abilityMods: ["+2", "+2", "+2", "+2", "+2", "+2"]
abilities_top:
  - name: "Planar Incarnation - Universe (The Remnants)"
    desc: "All shades are formed from and personify the nature of the plane on which they manifest, and their statistics are adjusted as summarized below. They also gain any trait associated with creatures from their plane. <br>  <br> **Universe (The Remnants)** The remnants are among the rarest of shades; appearing as plain, bland versions of their mortal selves. <br>  <br> - **Language** any one spoken in life (such as Common) <br> - **Additional Ability** [[Ferocity]] <br> - **Melee** fist +7, **Damage** 1d8+2 bludgeoning"
armorclass:
  - name: AC
    desc: "15; **Fort** +7, **Ref** +7, **Will** +7"
health:
  - name: HP
    desc: "22"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (unarmed), **Damage** 1d8+2 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The remnants are among the rarest of shades; appearing as plain, bland versions of their mortal selves.

When a mortal dies, their soul travels to the Boneyard in the Outer Planes where they're judged by Pharasma, the goddess of the dead. Once judged, their soul is sent on to their final reward or punishment and, in the process, transformed into a creature known as a shade. This transformation grants the soul a new body, one whose shape is determined by the prevailing philosophical forces of the plane to which they're sent. A shade's memories from their former life usually fade, reduced to a few hazy fragments akin to half-remembered dreams. Regardless of the shade's size, power, or nature in life, they're a Medium creature in their afterlife.

Existence as a shade can last for eons but isn't necessarily eternal. Deities, powerful denizens of the Great Beyond, or even the Outer Planes can further alter a shade's nature by either reducing them into raw quintessence, spiritual essence that's then used to expand a plane's physical manifestation, or by transforming them into a new form of supernatural life such as a celestial, monitor, or fiend. Should a shade die, their body breaks down in a process akin to decay, their form reverting to the elements that make up their plane. This represents the true end of a soul's journey—their life essence reuniting with the heart of the Great Beyond to be recycled into Creation's Forge, fueling the creation of new souls.

```statblock
creature: "Shade (Universe)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
