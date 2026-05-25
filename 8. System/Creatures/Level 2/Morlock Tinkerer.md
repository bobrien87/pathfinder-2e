---
type: creature
group: ["Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Morlock Tinkerer"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: ""
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
    desc: "Acrobatics +7, Athletics +8, Crafting +8, Stealth +9"
abilityMods: ["+4", "+3", "+1", "-2", "+3", "+1"]
abilities_top:
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
  - name: "Sneak Attack"
    desc: "A morlock's Strikes deal an extra 1d6 precision damage to [[Off Guard]] creatures."
  - name: "Swarming Stance"
    desc: "A morlock can share the same space as another morlock, but no more than two morlocks can occupy the same space. When morlocks share the same space, they gain a +1 circumstance bonus to attack rolls."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "40"
abilities_mid:
  - name: "+2 Status to All Saves vs. Disease and Poison"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +9 (`pf2:1`), **Damage** 1d6+4 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (agile, unarmed), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Club +8 (`pf2:1`) (thrown 10), **Damage** 1d6+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Instinctual Tinker"
    desc: "`pf2:2` The morlock tinkers with an adjacent construct or mechanical hazard. They attempt a [[Crafting]] check against the construct's or hazard's Fortitude DC. The morlock can't succeed if the target's level is more than double the morlock's. <br> - **Critical Success** The target gains 4d6 healing Hit Points and a +1 circumstance bonus to attack rolls for 1 minute. <br> - **Success** The target gains 2d6 healing Hit Points. <br> - **Critical Failure** The morlock injures itself, taking 2d6 damage (typically bludgeoning, piercing, or slashing, but potentially a different type at the GM's discretion). <br>  <br> > [!danger] Effect: Instinctual Tinker (Critical Success)"
  - name: "Leap Attack"
    desc: "`pf2:2` The morlock Strides up to twice its Speed, during which it attempts a [[High Jump]] or a [[Long Jump]]. At any point during its movement, the morlock can make a melee Strike against an enemy in its reach. <br>  <br> The morlock then can't use Leap Attack for 1 round."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Most morlocks have little talent for crafting, but many have an uncanny knack for tinkering. The sounds of machinery and moving parts tend to attract them. These morlocks particularly enjoy the ticking sounds of clockworks. Many tales from Darklands travelers describe morlocks who are able to take used or disabled mechanical traps and restore them, seemingly for the morlock's own satisfaction more than any desire to use the device.

Morlocks descended from humans who were lost among the dark, tangled tunnels of the upper reaches of the Darklands thousands of generations ago. Their eyes grew large and pale to absorb any speck of illumination. Their frames became wiry from an altered diet and their arms grew long, becoming perfect for the uncanny, four-limbed shuffle that lets them traverse the subterranean passages. However, their forms hide their strength and swiftness. Morlocks no longer remember the lives their ancestors led on the surface, although many of them dwell in shattered ruins that were swallowed by the earth. Some morlocks worship the statues of humans from these bygone eras as gods, but others now venerate Lamashtu, Rovagug, or other violent deities.

Morlocks typically stands just over 5 feet tall and weigh roughly 150 pounds.

```statblock
creature: "Morlock Tinkerer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
