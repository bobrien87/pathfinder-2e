---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Infernal Registrar"
level: "10"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19"
languages: "Common, Diabolic"
skills:
  - name: Skills
    desc: "Deception +22, Diplomacy +33, Religion +30, Society +33, Legal Lore +33, Scribe Lore +30"
abilityMods: ["+2", "+2", "+2", "+5", "+3", "+4"]
abilities_top:
  - name: "+14 to Sense Motive"
    desc: ""
  - name: "Contract Specialist"
    desc: "For encounters involving matters of contracts and dealings with Hell, the infernal registrar is an 18th-level challenge."
  - name: "Death is a Promotion"
    desc: "The infernal registrar does not fear death, as they have a signed infernal contract for immediate promotion to a mid-ranked devil upon their soul's arrival in Hell. They're immune to all Intimidation checks to [[Coerce]] involving threats of death."
  - name: "Friends in Low Places"
    desc: "Though devils do not respect most mortals, they respect the office of infernal registrar. No creature with the devil trait of 18th level or lower will knowingly and willingly attack an infernal registrar."
  - name: "Technically Correct"
    desc: "The infernal registrar uses their Legal Lore modifier on all Deception checks to Lie."
armorclass:
  - name: AC
    desc: "27; **Fort** +19, **Ref** +16, **Will** +33"
health:
  - name: HP
    desc: "180; **Resistances** fire 10"
abilities_mid:
  - name: "+2 Circumstance to All Saves vs. Fear"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff of Office +19 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+8 bludgeoning plus 1d6 fire"
  - name: "Melee strike"
    desc: "Fist +18 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**5th** [[Banishment]], [[Divine Immolation]]<br>**4th** [[Detect Scrying]], [[Suggestion]]<br>**3rd** [[Chilling Darkness]], [[Locate]], [[Ring of Truth]]<br>**2nd** [[Translate]] (At Will)<br>**1st** [[Detect Magic]], [[Fear]], [[Ignition]], [[Read Aura]]"
abilities_bot:
  - name: "A Favor for a Favor"
    desc: "`pf2:3` The infernal registrar has the authority to make limited infernal contracts with other mortals. They summon a contract with the legal language they desire. Detecting [[Hidden]] clauses in the contract requires a successful DC 43 [[Society]] check or a DC 38 Legal lore check. Once signed, the contract vanishes into the infernal filing system in Hell. The infernal registrar cannot grant any boons beyond their own personal power (usually limited to information, advice, or access to elements of the infernal bureaucracy)."
  - name: "Request Document"
    desc: "`pf2:3` The infernal registrar makes a request to summon a copy of any infernal contract a specific creature has signed. They must know enough information to specifically identify the individual who signed. The infernal registrar attempts a Legal lore check with a DC equal to a hard DC of the level of the creature in question. The infernal registrar will never promise a successful use of this ability in the agreements they make. Each agreement is typically for one attempt. Any copy summoned is simply a copy, has no impact on the original contract if destroyed or altered, and will vanish if taken more than 20 feet from the infernal registrar. <br> - **Critical Success** A copy of the contract appears before the infernal registrar after 10 minutes. <br> - **Success** A copy of the contract appears before the infernal registrar after 1 hour. <br> - **Failure** The attempt fails, but the infernal registrar can try again after 24 hours. <br> - **Critical Failure** The attempt fails, and the infernal registrar can't try again for the named creature for 1 year."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The infernal registrar is a mortal representative of Hell's bureaucracy. They can access copies of all infernal contracts signed by a denizen of their world and can navigate the machinations of Hell's many devils. They can grant special access—for a price.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Infernal Registrar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
