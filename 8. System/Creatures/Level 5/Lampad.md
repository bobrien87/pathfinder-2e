---
type: creature
group: ["Earth", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lampad"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Earth"
trait_02: "Fey"
trait_03: "Nymph"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Aklo, Common, Fey, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +9, Diplomacy +14, Nature +10, Occultism +11, Performance +14, Society +9, Stealth +12"
abilityMods: ["+0", "+5", "+4", "+2", "+3", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "85; **Weaknesses** cold iron 5"
abilities_mid:
  - name: "Cavern Dependent"
    desc: "A lampad is mystically bonded to a single cavern or other self-contained underground area and must remain within 300 feet of it. <br>  <br> If they move beyond that range, they become [[Sickened]] 1 and are unable to recover. They must attempt a DC 19 [[Fortitude]] save every hour or increase the sickened value by 1 (to a maximum of sickened 4). <br>  <br> After 24 hours, they become [[Drained]] 1, with this value increasing by 1 every additional 24 hours. A lampad can perform a 24-hour ritual to bond to a new cavern."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Earthen Fist +14 (`pf2:1`) (agile, finesse), **Damage** 2d10+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Light Wisp +14 (`pf2:1`) (magical, range 30 ft.), **Damage** 1d8+2 mental plus 1d6 fire plus 1d6 vitality"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 22, attack +0<br>**4th** [[Shape Stone]]<br>**3rd** [[One with Stone]] (At Will)<br>**2nd** [[Revealing Light]]<br>**1st** [[Heal]], [[Light]], [[Pummeling Rubble]]"
abilities_bot:
  - name: "Weep"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The lampad begins a heart-wrenching fit of weeping, inspiring sympathetic sobbing in nearby creatures. Each non-lampad creature within @Template[emanation|distance:30]{30 feet} who hears the lampad's weeping must succeed at a DC 20 [[Will]] save or be unable to use reactions for 1 round and [[Slowed]] 1 on its next turn as it sobs uncontrollably."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Lampads protect dark, hidden places underground. Not only do they defend subterranean caverns from threats, but they also safeguard well-meaning innocents from the dangers that lurk below the surface. Lampads are so-named for the wisps of magic light they often carry, guiding the lost to safety while luring threats to their doom. Lampads' mercurial nature makes their reactions difficult to predict, though they rarely demonstrate outright malice without sufficient provocation.

Nymphs are fey guardians of nature possessed of great beauty and forms that meld breathtaking humanoid features with the natural elements they guard. Nymph queens are powerful nymphs who rule over and protect a much greater territory of untouched wilderness. For instance, a lampad might guard a beautiful underground cavern, but a lampad queen might call an entire system of caves their domain.

```statblock
creature: "Lampad"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
