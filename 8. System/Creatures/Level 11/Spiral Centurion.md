---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spiral Centurion"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +23, Athletics +23"
abilityMods: ["+6", "+6", "+5", "-5", "+2", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "31; **Fort** +22, **Ref** +25, **Will** +16"
health:
  - name: HP
    desc: "170"
abilities_mid:
  - name: "Top-Heavy"
    desc: "A spiral centurion's top-like design makes it susceptible to effects that would cause it to fall [[Prone]]. The DC of any attempt to knock the spiral centurion prone is reduced by 5. If the spiral centurion attempts a check or saving throw to resist being knocked prone, it takes a –5 status penalty. A spiral centurion that has been knocked prone can't use any actions other than to attempt to Stand, but it must succeed at a DC 30 [[Acrobatics]] check to do so."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Blade +23 (`pf2:1`) (agile, sweep), **Damage** 2d12+12 slashing"
spellcasting: []
abilities_bot:
  - name: "Hurl Blade"
    desc: "`pf2:2` The spiral centurion hurls one of its blades with an angled spin to ensure a swooping flight path. The blade deals @Damage[6d6[slashing]|options:area-damage] damage to each creature in a @Template[type:line|distance:40] (DC 30 [[Reflex]] save). <br>  <br> At the start of the spiral centurion's next turn, the blade swoops around and returns along the same flight path, again dealing @Damage[6d6[slashing]|options:area-damage] damage (DC 30 [[Reflex]] save) to each creature along the same line."
  - name: "Rev Up"
    desc: "`pf2:1` **Requirements** The spiral centurion hasn't acted yet this turn <br>  <br> **Effect** The spiral centurion Strides up to its Speed. It then gains a +2 circumstance bonus to attack and damage rolls until the end of its turn."
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, blade, DC 30 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Whirling Death"
    desc: "`pf2:3` The spiral centurion spins furiously in place, its blades extended to slice through nearby creatures. It makes up to five melee blade Strikes. No single creature can be targeted by more than one blade Strike during one use of this ability. These attacks count toward the spiral centurion's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks are made."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These mechanical constructs were created to serve as guardians in an ancient and bygone era, although exactly who made them and the secrets of their construction have long since been lost to history. From the waist up, they resemble humanoids made of metal, but from the waist down, their bodies take the form of spinning metal tops ringed with blades that excel at cutting down nearby foes. Most spiral centurions can be directed to stand down with a password, but often these command phrases have been lost to the mists of time. In rare cases, a spiral centurion can also wield manufactured weapons or a shield in addition to its built-in weapons, giving it access to additional actions besides those listed below.

Most spiral centurions are hundreds or even thousands of years old, only staying functional because of the powerful magic used in their creation. Still, millennia of neglect have caused many spiral centurions to develop small glitches or malfunctions.

```statblock
creature: "Spiral Centurion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
