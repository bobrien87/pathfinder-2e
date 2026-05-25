---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Eremite"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+34; [[Greater Darkvision]], [[Truesight]] (precise) 5 feet"
languages: "Common, Diabolic, Shadowtongue (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +33, Deception +38, Diplomacy +36, Intimidation +40, Medicine +36, Religion +34, Stealth +36, Torture Lore +36"
abilityMods: ["+9", "+6", "+7", "+6", "+6", "+10"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Painsight"
    desc: "A velstrac automatically knows whether a creature it sees has any of the [[Doomed]], [[Dying]], and [[Wounded]] conditions as well as the value of those conditions."
  - name: "Shadow Traveler"
    desc: "When an eremite uses [[Interplanar Teleport]], they arrive at exactly their intended destination."
armorclass:
  - name: AC
    desc: "45; **Fort** +37, **Ref** +32, **Will** +34"
health:
  - name: HP
    desc: "375; **Immunities** cold, fear effects, nonlethal attacks; **Weaknesses** holy 20, silver 20"
abilities_mid:
  - name: "Regeneration 25 (Deactivated by Holy or Silver)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Ignore Pain"
    desc: "An eremite's actions can't be disrupted due to damage or Strikes (such as Reactive Strike)."
  - name: "Paralytic Perfection"
    desc: "30 feet. When a creature ends its turn in the aura, it feels compelled to offer pieces of its own flesh to the eremite. The creature must succeed at a DC 40 [[Will]] save or become [[Paralyzed]] for 1 round."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +39 (`pf2:1`) (magical, unholy), **Damage** 2d6 bleed plus 4d8+19 piercing plus [[Exquisite Pain]]"
  - name: "Melee strike"
    desc: "Claw +39 (`pf2:1`) (agile, magical, unholy), **Damage** 3d6+19 slashing plus 2d6 bleed plus [[Exquisite Pain]] plus [[Improved Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42, attack +34<br>**9th** [[Seize Soul]]<br>**7th** [[Interplanar Teleport (to the Netherworld or the Universe only)]], [[Planar Seal]], [[Warp Mind]]<br>**6th** [[Blessed Boundary]], [[Truesight]] (Constant)<br>**5th** [[Shadow Blast]], [[Shadow Blast]]<br>**4th** [[Translocate]] (At Will)<br>**1st** [[Harm]], [[Heal]], [[Stabilize]]"
abilities_bot:
  - name: "Evisceration"
    desc: "`pf2:1` **Requirements** The eremite has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The eremite excises flesh or bone from a creature they've grabbed or restrained. The target takes 6d10 persistent,bleed damage."
  - name: "Exquisite Pain"
    desc: "`pf2:1` An eremite's knowledge of pressure points and pain centers is unsurpassed. A creature hit by an eremite's melee Strikes must succeed at a DC 40 [[Fortitude]] save or be [[Stunned]] 2 ([[Stunned]] 4 on a critical failure). A creature that critically succeeds is temporarily immune for 24 hours."
  - name: "Focus Gaze"
    desc: "`pf2:1` The eremite stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against paralytic perfection. In addition, if the creature was already [[Paralyzed]], on a failed save, its unnatural longing causes it to become [[Doomed]] 1. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the eremite's next turn."
  - name: "Graft Flesh"
    desc: "`pf2:1` **Requirements** The eremite holds a piece of flesh they collected via Evisceration <br>  <br> **Effect** The eremite attaches the stolen flesh to themself. They either regain 100 Hit Points; reduce the value of their [[Clumsy]], [[Drained]], [[Enfeebled]], or [[Stupefied]] condition by 3; or reduce the stage of any affliction affecting them by 3."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`



```statblock
creature: "Eremite"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
