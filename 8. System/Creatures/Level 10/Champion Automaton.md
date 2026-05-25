---
type: creature
group: ["Automaton", "Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Champion Automaton"
level: "10"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Automaton"
trait_02: "Construct"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Common (One other language the champion knew in life usually jistkan, Telepathy 60 feet)"
skills:
  - name: Skills
    desc: "Athletics +22, Diplomacy +18, Intimidation +18"
abilityMods: ["+6", "+5", "+5", "+3", "+4", "+4"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "29; **Fort** +21, **Ref** +19, **Will** +17"
health:
  - name: HP
    desc: "170; **Resistances** physical 10 except adamantine"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pincer +23 (`pf2:1`) (magical), **Damage** 2d12+12 piercing plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Energy Beam +23 (`pf2:1`) (fire, magical), **Damage** 2d10+10 fire"
spellcasting: []
abilities_bot:
  - name: "Arcane Slam"
    desc: "`pf2:1` **Requirements** The champion has a creature [[Grabbed]] <br>  <br> **Effect** The champion channels supernatural energy through its pincers, then slams its foe against the ground. The grabbed creature takes 3d6 bludgeoning and 3d6 fire damage, is knocked [[Prone]] and must attempt a DC 29 [[Fortitude]] save. On a failure the target is [[Enfeebled]] 1 ([[Enfeebled]] 2 on a critical failure) from the force of the slam. At the end of the Arcane Slam, the grapple ends."
  - name: "Spinning Toss"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Requirements** The champion has a creature [[Grabbed]] <br>  <br> **Effect** The champion spins on its axis, using the creature it's holding as an impromptu bludgeon before tossing it aside. The champion attempts an Athletics check against the grabbed creature's Fortitude DC. <br> - **Critical Success** The champion fings its victim. The grapple ends. The grabbed creature is thrown into a space within 10 feet, takes 8d6 bludgeoning damage, and falls [[Prone]]. All creatures adjacent to the champion take the same amount of bludgeoning damage (DC 29 [[Reflex]] save). <br> - **Success** As critical success, except the grabbed creatures is thrown into a space within 5 feet, and creatures take 4d6 bludgeoning damage. <br> - **Failure** The champion tosses its victim aside. The grapple ends. The grabbed creature falls prone. <br> - **Critical Failure** The champion fumbles its grasp on its victim and the grapple ends."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The artifcers of Jistka crafted warrior automatons to fght on the front lines of their armies, and in this goal they succeeded admirably. Brutal, effective combatants, champion automatons contain the souls of the best of the Imperium's armies, its most dedicated soldiers and respected offcers, all rendered deadlier than ever before in their bodies of metal and magic.

```statblock
creature: "Champion Automaton"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
