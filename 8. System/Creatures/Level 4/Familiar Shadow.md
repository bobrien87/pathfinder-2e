---
type: creature
group: ["Incorporeal", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Familiar Shadow"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Necril"
skills:
  - name: Skills
    desc: "Acrobatics +10, Stealth +14"
abilityMods: ["-5", "+4", "+0", "-2", "+2", "+3"]
abilities_top:
  - name: "Slink in Shadows"
    desc: "The shadow can [[Hide]] or end its [[Sneak]] in a creature's or object's shadow."
armorclass:
  - name: AC
    desc: "20; **Fort** +8, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "40; void healing; **Immunities** death effects, disease, paralyzed, poison, precision, unconscious, bleed; **Resistances** all damage 5 except force, ghost touch, vitality, spirit"
abilities_mid:
  - name: "Light Vulnerability"
    desc: "Attacks against the shadow are treated as magical if made by a creature who is in magical light or with an object that is in magical light (such as from the [[Light]] spell)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shadow Hand +15 (`pf2:1`) (finesse, magical), **Damage** 2d6+3 void"
spellcasting: []
abilities_bot:
  - name: "Infest Shadow"
    desc: "`pf2:2` **Requirements** The familiar shadow is adjacent to the PC whose image it duplicates, that PC is not in darkness or [[Invisible]], and the familiar shadow is aware of the PC <br>  <br> **Effect** The familiar shadow attempts to infest the shadow of the PC whose appearance it has. The familiar shadow twists and writhes against the PC's shadow before pulling back, and the targeted PC must attempt a DC 21 [[Will]] save with the following results. <br> - **Critical Success** The PC is unaffected and is immune to further attempts to Infest Shadow. <br> - **Success** The PC is unaffected. <br> - **Failure** The familiar shadow leaves its unholy influence behind in the PC's shadow, infesting it. The PC's shadow writhes and twists on its own, as if willfully ignoring the actions of the character to whom it's attached. The infested shadow has a habit of making distracting and embarrassing motions and imparts a –2 status penalty to its attached PC's Deception, Diplomacy, and Stealth checks. If the PC is in a situation where they aren't casting a shadow (such as when they're in complete darkness or are invisible), these penalties are suppressed, but they return as soon as their infested shadow does. If a PC with an infested shadow gains the dying condition, the shadow breaks free and becomes a shadow spawn (which functions the same as a shadow spawn created by a typical shadow). This shadow spawn won't attack the creature it spawned from, but any other targets are fair game. If the dying character recovers, their shadow spawn immediately dies, and their shadow returns to normal—otherwise, the only way to be rid of this strange curse is through the use of a spell like cleanse affliction, as it has an unlimited duration. <br> - **Critical Failure** As failure, but the penalties apply to all checks made by the PC."
  - name: "Steal Shadow"
    desc: "`pf2:1` **Requirements** The famliar shadow hit a living creature it is duplicating with a shadow hand Strike on its previous action <br>  <br> **Effect** The famliar shadow pulls at the target's shadow, making the creature [[Enfeebled]] 1. This is cumulative with other enfeebled conditions from shadows, to a maximum of [[Enfeebled]] 4. If this increases a creature's enfeebled value to 3 or more, the target's shadow is separated from its body (see shadow spawn). The enfeebled value from Steal Shadow decreases by 1 every hour."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The mysterious undead known as shadows lurk in dark places and feed on those who stray too far from the light.

```statblock
creature: "Familiar Shadow"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
