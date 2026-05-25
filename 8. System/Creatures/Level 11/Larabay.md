---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Larabay"
level: "11"
rare_01: "Common"
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
    desc: "+22; [[Low-Light Vision]]"
languages: "Common, Fey, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +23, Athletics +17, Deception +24, Diplomacy +22, Nature +19, Performance +22, Thievery +23"
abilityMods: ["+2", "+6", "+3", "+4", "+4", "+7"]
abilities_top:
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Befuddling Visions"
    desc: "The larabay's gaze creates disorientation and confusion. A creature hit by befuddling gaze must attempt a Will save. <br> - **Critical Success** The target is unaffected and temporarily immune to befuddling visions for 1 minute. <br> - **Success** The target is unaffected. <br> - **Failure** The target becomes clumsy and [[Dazzled]] for 1 round. <br> - **Critical Failure** The target becomes [[Confused]] for 1 round, and clumsy and dazzled for 1 round afterward."
armorclass:
  - name: AC
    desc: "30; **Fort** +18, **Ref** +24, **Will** +21"
health:
  - name: HP
    desc: "175; **Weaknesses** cold iron 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +23 (`pf2:1`) (deadly d8, disarm, finesse, magical), **Damage** 2d6+12 piercing plus [[Mischief]]"
  - name: "Ranged strike"
    desc: "Befuddling Gaze +22 (`pf2:1`) (magical, mental, visual), **Damage** 2d8+10 mental plus [[Befuddling Visions]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30, attack +22<br>**6th** [[Cursed Metamorphosis]]<br>**5th** [[Hallucination]], [[Illusory Scene]]<br>**2nd** [[Invisibility]] (At Will)<br>**1st** [[Figment]], [[Illusory Object]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The larabay can take on the appearance of a specific Medium or Small humanoid. This removes their fly Speed but doesn't change the attack and damage modifiers with their Strikes."
  - name: "Mischief"
    desc: "`pf2:1` **Requirements** The larabay's last action was a successful rapier Strike <br>  <br> **Effect** The larabay attempts to [[Disarm]] the creature they hit. They gain a +4 status bonus to the Athletics check. This attempt neither applies nor counts toward the larabay's multiple attack penalty."
  - name: "Rainbow Flight"
    desc: "`pf2:2` The larabay Flies up to its fly Speed, creating a stunning rainbow in its wake. This movement doesn't provoke reactions. Any creature adjacent to the larabay at any point during this movement must attempt a DC 30 [[Will]] save saving throw to resist staring at the magnificent rainbow. The larabay cannot use Rainbow Flight again for 1d4 rounds. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is [[Dazzled]] for 1 round. <br> - **Failure** The target is dazzled for 1 round and [[Slowed]] 1. <br> - **Critical Failure** The target is dazzled for 1 minute and [[Slowed]] 2."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Larabays are bright-eyed, humanoid-looking fey with colorful wings and needlelike teeth who generally reside along warm coastal regions and islands. Like other fey, they enjoy lavish pranks and fantastical illusions that create chicanery and confusion. A larabay's desire for a joke can sometimes reach dire extremes, such as employing illusions to lure ships into rocks and travelers off cliffs. While some have fortuitously become heroes by playing pranks on tyrants or cruel people, this is almost entirely coincidental, as larabays do not often consider the morals or goals of their targets; they simply enjoy the fruits of their chaos.

```statblock
creature: "Larabay"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
