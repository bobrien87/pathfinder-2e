---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Meladaemon"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]], [[Lifesense]] (imprecise) 30 feet"
languages: "Common, Daemonic (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +20, Athletics +21, Deception +23, Intimidation +23, Religion +20, Stealth +23, Survival +19"
abilityMods: ["+7", "+5", "+6", "+3", "+4", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Daemonic Famine"
    desc: "**Saving Throw** DC 29 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1 day) <br>  <br> **Stage 2** [[Enfeebled]] 1 (1 day) <br>  <br> **Stage 3** [[Enfeebled]] 2 (1 day) <br>  <br> **Stage 4** as stage 3 <br>  <br> **Stage 5** [[Enfeebled]] 3 (1 week) <br>  <br> **Stage 6** dead"
  - name: "Withering Touch"
    desc: "When the meladaemon hits with a claw Strike or a creature begins its turn grabbed by the meladaemon, the creature must attempt a DC 30 [[Fortitude]] save. On a failure, the creature takes 1d6 void damage and becomes [[Fatigued]]. This fatigue ends when the creature drinks."
armorclass:
  - name: AC
    desc: "31; **Fort** +23, **Ref** +20, **Will** +19"
health:
  - name: HP
    desc: "225; **Immunities** death effects; **Weaknesses** holy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Consumptive Aura"
    desc: "20 feet. A meladaemon emanates an aura of intense hunger. Each round a creature begins its turn in the aura, it must attempt a DC 27 [[Fortitude]] save. On a failure, the creature takes 1d6 void damage (2d6 void damage on a critical failure) and becomes [[Fatigued]]. This fatigue ends as soon as the creature eats any food."
  - name: "Withering Opportunity"
    desc: "`pf2:r` **Trigger** The meladaemon is attacked by an adjacent creature and the attack misses <br>  <br> **Effect** The meladaemon swipes at the triggering creature, which must immediately attempt a save against the meladaemon's withering touch."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +24 (`pf2:1`) (magical, reach 10 ft., unholy), **Damage** 2d12+16 piercing plus [[Daemonic Famine]]"
  - name: "Melee strike"
    desc: "Claw +24 (`pf2:1`) (agile, magical, reach 10 ft., unarmed, unholy), **Damage** 2d8+16 slashing plus [[Grab]] plus [[Withering Touch]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 31, attack +21<br>**4th** [[Translocate]], [[Translocate (At will)]]<br>**1st** [[Fear]], [[Force Barrage (At will)]], [[Phantom Pain]]"
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Meladaemons personify death by starvation and thirst, and revel in spreading the same despair that brought about their mortal demise. When they aren't blighting fields, massacring livestock, or tainting water supplies, they experiment on prisoners to study how long creatures can go without sustenance and the deleterious effects that result from such deprivation. Fiercely loyal to Trelmarixian, Horseman of Famine, they serve no other beings. They work alongside other daemons if Trelmarixian wills it, but are notoriously traitorous.

```statblock
creature: "Meladaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
