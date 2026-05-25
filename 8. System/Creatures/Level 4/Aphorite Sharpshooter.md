---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aphorite Sharpshooter"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Nephilim"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Utopian"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +8, Deception +10, Diplomacy +10, Intimidation +10, Engineering Lore +12"
abilityMods: ["+2", "+4", "+2", "+1", "+0", "+2"]
abilities_top:
  - name: "Calculated Reload"
    desc: "When the sharpshooter reloads their crossbow, they also calculate the best angle to their target, increasing the damage die from 1d8 to 1d10 and gaining a +2 circumstance bonus to their damage roll for their next crossbow Strike, as long as it occurs before the end of their next turn."
armorclass:
  - name: AC
    desc: "21; **Fort** +10, **Ref** +12, **Will** +8"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Crystalline Dust"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The sharpshooter becomes [[Concealed]] for 4 rounds, though they can't use the concealment to Hide or [[Sneak]], as normal for concealment where their position is obvious."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +14 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+8 piercing"
  - name: "Ranged strike"
    desc: "Crossbow +14 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d8+6 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 18, attack +10<br>**1st** [[Sure Strike]]"
abilities_bot:
  - name: "Hurtful Critique"
    desc: "`pf2:1` The sharpshooter makes witty but disparaging comments about the fighting style of a target within 30 feet, expressing sympathy over every missed blow and providing sarcastic advice on how to improve. <br>  <br> The target must succeed at a DC 18 [[Will]] save or take a –1 circumstance penalty to attack rolls (–2 on a critical failure) for 1 minute or until it makes a successful Strike against the sharpshooter. <br>  <br> A creature that critically succeeds or who Strikes the sharpshooter after failing is immune to that sharpshooter's Hurtful Critique for 1 hour. <br>  <br> > [!danger] Effect: Hurtful Critique"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The denizens of the Eternal City of Axis first forged aphorites to serve as emissaries, agents, and facilitators, with one foot in the sublime, perfect order, and one in the messy, murky, confusing muck of the Universe. In time, aphorites spread across the length and breadth of Golarion. Today, they can be found in any corner of any land, and only a fraction still serve Axis directly.

Aphorites, like all nephilim, stand out quite vividly from their fellow mortals, sporting metallic skin, a faint coating of crystalline dust, a swirl of mathematical symbols, or perfectly symmetrical features. Many aphorites think logically and find satisfaction in careers dealing with numbers and information. Often, this leads them to become bookkeepers, clerks, or architects, but some become military engineers or sharpshooters. Others are drawn to the art of production, becoming blacksmiths, carpenters, engineers, architects, tailors, masons, or other such artisans. But no matter their careers, aphorites often feel the urge to tinker, and aphorite inventions draw both mockery and appreciation in equal measure.

Aphorites who work in less academic professions, such as mercenaries or laborers, sometimes hide their keen analytical intelligence beneath extravagant demeanors and flamboyant hats. Some craft even these disguises with the same depth and complexity they do other aspects of their lives, considering every theatrical mannerism carefully and planning out their every detail.

Nephilim are individuals infused with the essence of an immortal being from the Outer Planes, such as a celestial, fiend, or monitor. While the examples presented here are humans with nephilim heritages that trace back to Axis and the Maelstrom, members of nearly any ancestry can be born with an influx of similar energies and become a planar scion. More about nephilim can be found starting on page 78 of Player Core, and other nephilim NPCs are presented beginning on page 266 of Monster Core.

```statblock
creature: "Aphorite Sharpshooter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
