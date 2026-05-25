---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sordesdaemon"
level: "15"
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
    desc: "+26; [[Darkvision]]"
languages: "Common, Daemonic (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +27, Crafting +29, Intimidation +28, Medicine +26, Religion +28, Stealth +24, Survival +28"
abilityMods: ["+8", "+3", "+9", "+6", "+5", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Pollution Infusion"
    desc: "Non-fiend creatures adjacent to the afflicted creature take a -1 circumstance penalty to saving throws against disease <br>  <br> **Saving Throw** DC 36 [[Fortitude]] save <br>  <br> **Stage 1** [[Drained]] 1 (1 day) <br>  <br> **Stage 2** [[Doomed]] 1 and [[Drained]] 1 (1 day) <br>  <br> **Stage 3** [[Doomed]] 1 and [[Drained]] 2 (1 day) <br>  <br> **Stage 4** [[Doomed]] 2 and [[Drained]] 2 (1 week) <br>  <br> **Stage 5** dead. <br>  <br> > [!danger] Effect: Pollution Infusion"
armorclass:
  - name: AC
    desc: "37; **Fort** +30, **Ref** +24, **Will** +26"
health:
  - name: HP
    desc: "300; **Immunities** death effects, disease; **Weaknesses** holy 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Miasma of Pollution"
    desc: "30 feet. A creature that enters the aura or begins its turn in it must succeed at a DC 34 [[Fortitude]] save or be [[Sickened]] 2 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). Creatures in the aura can't reduce the value of the sickened condition. A creature that succeeds at its save is temporarily immune for 1 minute. Creatures made of water (such as water elementals) and plant creatures use an outcome one degree of success worse than the result of their save."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +29 (`pf2:1`) (magical, reach 15 ft., unarmed, unholy), **Damage** 3d8+14 bludgeoning plus 1d6 spirit plus [[Pollution Infusion]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +28<br>**8th** [[Desiccate]], [[Spiritual Epidemic]]<br>**5th** [[Toxic Cloud]] (At Will)<br>**4th** [[Translocate]], [[Translocate]] (At Will)"
abilities_bot:
  - name: "Retch of Foulness"
    desc: "`pf2:2` The sordesdaemon exhales a spray of sewage that deals @Damage[8d6[acid],8d6[poison]|options:area-damage]{8d6 acid damage and 8d6 poison damage} in a @Template[cone|distance:30] (DC 36 [[Fortitude]] save). <br>  <br> It can't use Retch of Foulness again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sordesdaemons are hulks of sewage and daemonic flesh that embody death through pollution. They are among the newest types of daemons to appear on Golarion and are constantly surrounded by a cloud of foul mist that chokes living creatures. Sordesdaemons are fiendishly clever and often seek to inspire mortals with new ideas and inventions that despoil the environment. While these daemons are more than capable of ruining habitats on their own, they take great delight in encouraging mortals to do so themselves, as the act can eventually create new sordesdaemons. Once a given forest, river or other natural abode is completely polluted, a sordesdaemon often moves to claim it as their domain.

```statblock
creature: "Sordesdaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
