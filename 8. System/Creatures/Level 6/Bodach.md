---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bodach"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Low-Light Vision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +11, Deception +15, Diplomacy +11, Intimidation +13, Nature +13, Stealth +13, Thievery +15"
abilityMods: ["+2", "+2", "+4", "+4", "+3", "+4"]
abilities_top:
  - name: "Unstoppable"
    desc: "A bodach reduces any penalty it takes to its Speed by 5 feet (to a minimum of 0 feet). A bodach can fit into tight spaces as if it were a Small creature. It can move at its full Speed while [[Squeezing]]."
armorclass:
  - name: AC
    desc: "23; **Fort** +14, **Ref** +12, **Will** +17"
health:
  - name: HP
    desc: "110; **Weaknesses** cold iron 5"
abilities_mid:
  - name: "Gray Aura"
    desc: "15 feet. The bodach is always surrounded by a pall of gloomy gray, like the air before it rains. A non-fey or non-hag creature entering the aura or beginning their turn in the aura must succeed at a DC 21 [[Will]] save or become [[Slowed]] 1 for 1 round ([[Slowed]] 2 on a critical failure). A creature who succeeds is temporarily immune to the aura for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +16 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+6 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 24, attack +0<br>**2nd** [[Mist]] (At Will)"
abilities_bot:
  - name: "Implacable Curse"
    desc: "`pf2:2` The bodach makes a staff Strike. If it hits, it deals an additional 2d8 spirit damage, and the target must attempt a save against either Mumbletongue or Stumblefoot (the bodach's choice)."
  - name: "Mumbletongue"
    desc: "`pf2:2` The bodach mumbles a string of half-comprehensible nonsense, cursing creatures within a @Template[type:emanation|distance:10]. Each creature in the area must succeed at a DC 24 [[Will]] save or become [[Stupefied 1]] for 1 minute ([[Stupefied 2]] on a critical failure)."
  - name: "Stumblefoot"
    desc: "`pf2:2` The bodach stares unblinkingly at its foes, cursing creatures within a @Template[type:cone|distance:15]. Each creature in the area must succeed at a DC 24 [[Fortitude]] save or become [[Clumsy]] 1 and [[Enfeebled]] 1 for 1 minute ([[Clumsy]] 2 and [[Enfeebled]] 2 on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`



```statblock
creature: "Bodach"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
