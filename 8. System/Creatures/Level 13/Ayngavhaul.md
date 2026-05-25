---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ayngavhaul"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Greater Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +27, Deception +26, Diplomacy +24, Religion +24, Library Lore +24"
abilityMods: ["+4", "+4", "+5", "+8", "+5", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Personal Library"
    desc: "Any tomes an ayngavhaul is reading or referencing for their current work can be stored in the devil's personal library, a floating collecting of tomes revolving around the devil that can be used offensively or defensively. Retrieving or returning a tome requires an Interact action."
  - name: "Poison Minds"
    desc: "Creatures hit by the ayngavhaul's searing words must succeed at a DC 33 [[Will]] save saving throw or become [[Stupefied 1]] for 1 round (or [[Stupefied 2]] on a critical failure). If the target is trained in Religion, they take a –2 circumstance penalty to their save."
armorclass:
  - name: AC
    desc: "34; **Fort** +23, **Ref** +20, **Will** +26"
health:
  - name: HP
    desc: "240; **Immunities** fire; **Weaknesses** holy 10; **Resistances** physical 10 except silver"
abilities_mid:
  - name: "Spellblock Tome"
    desc: "`pf2:r` **Trigger** The ayngavhaul is targeted by a spell <br>  <br> **Effect** The ayngavhaul flings a tome from its personal library at the spell. The devil must attempt a DC 5 flat check. On a success, the tome fully absorbs the effects of the spell and burns up into a harmless pile of ash. Regardless of the result, the devil can't use this ability again for 1d4 rounds."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +25 (`pf2:1`) (magical, unholy), **Damage** 3d8+8 slashing"
  - name: "Ranged strike"
    desc: "Searing Words +27 (`pf2:1`) (auditory, magical, unholy), **Damage** 1d6 fire plus 3d10+8 mental plus [[Poison Minds]]"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 33, attack +25<br>**6th** [[Dominate]], [[Never Mind]]<br>**5th** [[Banishment]], [[Mind Probe]], [[Subconscious Suggestion]]<br>**1st** [[Daze]], [[Detect Magic]], [[Figment]], [[Phase Bolt]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Herald Heresy"
    desc: "`pf2:2` The ayngavhaul imparts blasphemous thoughts into the minds of all non-devil creatures within a @Template[type:burst|distance:20] up to 60 feet away. An affected creature takes @Damage[2d10[mental]|options:area-damage] damage plus @Damage[2d10[spirit]|options:area-damage] damage and must attempt a DC 33 [[Will]] save. Affected creatures gain a cumulative +1 circumstance bonus (up to a total of +4) to saves against all future attempts to Herald Heresy for 1 minute, as they become inured to the blasphemies. <br> - **Critical Success** The creature is unaffected and becomes temporarily immune for 1 hour. <br> - **Success** The creature takes half damage. <br> - **Failure** The creature takes full damage and becomes [[Slowed]] 1. <br> - **Critical Failure** The creature takes double damage and becomes [[Slowed]] 2."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Where a bright mind seeking knowledge becomes corrupted by eloquent lies and twisted truths, an ayngavhaul is sure to lurk. Often donned in the holy vestments of other faiths in a twisted mockery of their principles, these wily, well-read devils delight in using their knowledge to twist religious texts and teachings into the dangerous principles those same texts warn against. While many ayngavhauls develop advanced knowledge of unique specializations, there are many whose depth of knowledge of a single religion rivals that of even the most wizened priests.

Any information an ayngavhaul has read or learned is added to a massive living tome unique to the ayngavhaul. The information contained sorts itself based on the topic and point its owner is making.

While these devils spend most of their time in the libraries of Hell, they are most often summoned in desperate bids by students seeking lost or forbidden knowledge, and such knowledge comes with a cost. These devils use truths and loose interpretations of texts to lend credence to their heretical viewpoints. When these once-bright intellectuals are corrupted into blasphemous priests, tyrants, and despots spreading the twisted words of an ayngavhaul, that devil gains influence and renown within the scholarly circles of Hell.

```statblock
creature: "Ayngavhaul"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
