---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vermlek"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Chthonian, Draconic, Empyrean (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +10, Deception +7, Stealth +8"
abilityMods: ["+3", "+1", "+4", "+0", "+1", "+2"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Unsettling Movement"
    desc: "Whenever the vermlek Abandons a Body or Inhabits a Body, all creatures within @Template[emanation|distance:30]{30 feet} who can see the vermlek must succeed at a DC 19 [[Will]] save or become [[Frightened]] 1. On a critical failure, the creature is frightened 1 and [[Sickened]] 1. Regardless of the result, creatures are immune to the same vermlek's unsettling movement for 24 hours."
armorclass:
  - name: AC
    desc: "16 (19 while Inhabiting a Body); **Fort** +11, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "55; **Weaknesses** cold iron 5, holy 5, sonic 5"
abilities_mid:
  - name: "Recoil from Wasted Opportunities"
    desc: "Vermleks can't stand the sight of a good meal presented and then swiftly taken away. Whenever a [[Dying]] creature within sight of the vermlek has its dying condition removed, the vermlek takes 1d6 mental damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +12 (`pf2:1`) (unarmed, unholy), **Damage** 2d8+3 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, unarmed, unholy), **Damage** 2d6+3 bludgeoning"
  - name: "Melee strike"
    desc: "Longsword +12 (`pf2:1`) (unholy, versatile p), **Damage** 1d8+4 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 19, attack +0<br>**1st** [[Fear]], [[Harm]]"
abilities_bot:
  - name: "Abandon Body"
    desc: "`pf2:2` **Requirements** The vermlek is Inhabiting a Body <br>  <br> **Effect** The vermlek crawls out of the body they are inhabiting, devouring much of the body's remaining flesh and regaining 10 healing Hit Points in the process. The corpse they leave behind is little more than a husk."
  - name: "Inhabit Body"
    desc: "`pf2:3` **Requirements** The vermlek isn't already Inhabiting a Body <br>  <br> **Effect** The vermlek crawls into the body of an adjacent Medium humanoid that has been dead for no more than 1 week, consuming the bulk of the victim's skeleton and internal organs as they do so and cramming themself into the cavity. As long as they Inhabit a Body, the vermlek loses their bite attack, can wield weapons like a humanoid, gains a +3 circumstance bonus to AC, and gains a +3 circumstance bonus to Deception checks to `act impersonate options=impersonate-inhabited-creature` the creature they are inhabiting."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Vermleks, also called worm demons, manifest from the souls of mortals who desecrated the dead, such as grave robbers or necromancers. These fiends take their violations to a new extreme, using their demonic powers to horrifically core their living victims and don the flesh husk that remains.

In their natural form, a vermlek resembles an oversized pinkish worm with four long tails that end in writhing fibrils. Their mouth splits into four segments like a profane tulip lined with rows of dozens of pointed teeth. However, these fiends are often encountered only after they have crawled into the body of a dead humanoid and made the hollowed-out flesh their temporary host. Vermleks use their powers of deception and disguise to infiltrate mortal settlements and influence unwitting acquaintances of the bodies they wear. Particularly intelligent or conniving vermleks might even reach stations of real power within the ranks of an army or government, at which point exposure of their true form can wreak havoc among the populace they have so thoroughly duped.

```statblock
creature: "Vermlek"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
