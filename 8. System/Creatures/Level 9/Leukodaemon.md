---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Leukodaemon"
level: "9"
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
    desc: "+20; [[Darkvision]]"
languages: "Daemonic (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +18, Intimidation +18, Medicine +20, Religion +20, Stealth +18, Survival +16"
abilityMods: ["+6", "+5", "+1", "+3", "+5", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Plaguesense (Imprecise) 60 feet"
    desc: "A leukodaemon senses any creature with a disease, and they know the type and current stage of all diseases carried by any creature within range."
  - name: "Daemonic Pestilence"
    desc: "The leukodaemon can telepathically communicate with the afflicted creature at any distance on the same plane <br>  <br> **Saving Throw** DC 28 [[Fortitude]] save <br>  <br> **Stage 1** carrier (1 day) <br>  <br> **Stage 2** [[Drained]] 1 (1 day) <br>  <br> **Stage 3** [[Drained]] 2 (1 day) <br>  <br> **Stage 4** drained 2 (1 day) <br>  <br> **Stage 5** [[Drained]] 3 (1 week) <br>  <br> **Stage 6** dead"
armorclass:
  - name: AC
    desc: "28; **Fort** +15, **Ref** +21, **Will** +19"
health:
  - name: HP
    desc: "155; **Immunities** death effects, disease; **Weaknesses** holy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Infectious Aura"
    desc: "30 feet. <br>  <br> Leukodaemons radiate infection. All creatures within 30 feet of a leukodaemon take a –2 status penalty to saves against disease. If a creature within range contracts or progresses a disease, all adjacent creatures are exposed to the same disease, at the same DC. <br>  <br> > [!danger] Effect: Infectious Aura"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (disease, magical, reach 10 ft., unarmed, unholy), **Damage** 2d12+9 piercing plus [[Daemonic Pestilence]]"
  - name: "Melee strike"
    desc: "Claw +21 (`pf2:1`) (agile, disease, magical, reach 10 ft., unarmed, unholy), **Damage** 2d8+9 slashing plus [[Daemonic Pestilence]]"
  - name: "Ranged strike"
    desc: "Composite Longbow +21 (`pf2:1`) (deadly d10, disease, magical, propulsive, reload 0, unholy, volley 30, range 100 ft.), **Damage** 2d8+9 piercing plus [[Daemonic Pestilence]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26, attack +18<br>**4th** [[Translocate]], [[Translocate]] (At Will)<br>**2nd** [[Dispel Magic]]"
abilities_bot:
  - name: "Plague Breath"
    desc: "`pf2:2` The leukodaemon exhales a cloud of corpse-bloated, biting black flies in a @Template[cone|distance:20]. Creatures within the cone take @Damage[4d8[piercing]|options:area-damage] damage (DC 28 [[Reflex]] save). A creature that fails the save becomes [[Sickened]] 1 (or [[Sickened]] 2 on a critical failure)."
  - name: "Quicken Pestilence"
    desc: "`pf2:1` The leukodaemon coaxes a disease into full bloom. They choose a target in their aura of pestilence that's currently affected by a disease. That creature must attempt a Fortitude save against the disease as if the interval for the disease's current stage had passed."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These skull-headed, vulture-winged daemons are harbingers of pestilence and servants of their patron Apocalypse Rider, Apollyon. Manifestations of evil souls who perished from disease in life, leukodaemons work tirelessly alongside one another to spread disease across all the worlds of the multiverse.

Denizens of the bleak and terrible plane of Abaddon, daemons are shaped by and devoted to the destruction of life in all its forms. They seek the death of every mortal being by the most painful and horrible means possible, in service to the Apocalypse Riders. Each kind of daemon represents a different way to die, and their powers are nearly always aimed at spreading that particular form of death. Through the use of these powers, they seek to drag all existence down into a pit of hopelessness and despair, and to commit all souls to oblivion.

While mortals who summon daemons usually seek to use the creatures' destructive and corrupting powers for their own ends, daemons always look for ways to spread fear, doubt, and despair wherever they go. Often, daemons disguise their plots as the workings of other fiends, knowing that such confusion compounds mortals' fear and keeps those mortals from bringing the most effective weapons. As a result, learned mortals sometimes refer to daemons as "riders" after their leaders or "soul mongers" after their largest industry.

While many fiends seek to tempt mortals into lives of nihilistic evil to increase their own numbers and power on their native planes, daemons are further driven by a supernatural hunger for mortal souls and use a variety of methods—not least of which is the cacodaemons' soul gems—to entrap them. On Abaddon and in other forbidding places across the multiverse, souls are simultaneously a delicacy, a trade good, and a source of magical power, and the daemons are among the greatest gluttons, merchants, and abusers of this spiritual "resource."

```statblock
creature: "Leukodaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
