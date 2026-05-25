---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zebub"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Greater Darkvision]]"
languages: "Diabolic, Draconic, Empyrean (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +10, Arcana +7, Deception +8, Religion +9, Stealth +10"
abilityMods: ["+1", "+4", "+1", "+0", "+3", "+1"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Cocytan Filth"
    desc: "**Saving Throw** DC 18 [[Fortitude]] save <br>  <br> **Onset** 1d4 days <br>  <br> **Stage 1** [[Enfeebled]] 1 (1 day) <br>  <br> **Stage 2** [[Enfeebled]] 2 (1 day) <br>  <br> **Stage 3** [[Enfeebled]] 3 (1 day)"
  - name: "Sneak Attack"
    desc: "The zebub's Strikes deal an additional 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +10, **Will** +8"
health:
  - name: HP
    desc: "30; **Immunities** fire; **Weaknesses** holy 5; **Resistances** physical 5 except silver, poison 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +12 (`pf2:1`) (finesse, magical, unholy), **Damage** 1d10+5 piercing plus [[Cocytan Filth]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +7<br>**4th** [[Translocate]], [[Translocate]] (At Will)<br>**2nd** [[Invisibility (at will, self only)]]<br>**1st** [[Message]], [[Summon Animal (swarm creatures only)]]"
abilities_bot:
  - name: "Diabolic Eye"
    desc: "`pf2:3` The zebub records everything they see, and though they don't remember all observations, they can pass them along to another creature. <br>  <br> The zebub replays 10 minutes of witnessed events to a touched willing creature, which receives the memories in a flash of information. By remaining in contact, the zebub can spend additional 3-action activities to replay more information. <br>  <br> After relaying their visions to another, the zebub can't ever recall those events again."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Zebubs serve as Hell's messengers and spies. Their ability to share what they've seen with other creatures makes them especially useful—not only to other devils but also to mortal conjurers. Some infernal lords unleash them in enormous, horrid swarms upon unsuspecting lands to debase flesh and land alike while collecting secrets the infernal host might later put to use. Zebubs use any opportunity to manipulate weak-willed or easily tempted mortals into serving the zebubs' whims.

While arrogant and deceitful, zebubs lack the cunning and confidence of most devils, and thus their schemes often focus on satisfying self-serving or self-destructive ambitions. Zebubs form from the souls of childish and craven mortals, reshaped by the archdevil Baalzebul in the frozen, filthy wastes of Hell's seventh layer, Cocytus.

```statblock
creature: "Zebub"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
