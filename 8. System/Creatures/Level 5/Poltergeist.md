---
type: creature
group: ["Incorporeal", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Poltergeist"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Spirit"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +14, Intimidation +15, Stealth +14"
abilityMods: ["-5", "+5", "+0", "-1", "+2", "+4"]
abilities_top:
  - name: "Site Bound"
    desc: "A poltergeist is tied to a location and can't travel more than 120 feet from the place where it was created or formed. Some poltergeists are instead bound to a specific room, building, or similar area"
armorclass:
  - name: AC
    desc: "22; **Fort** +9, **Ref** +14, **Will** +13"
health:
  - name: HP
    desc: "55; void healing, rejuvenation; **Immunities** death effects, disease, paralyzed, poison, precision, unconscious, bleed; **Resistances** all damage 5 except force, ghost touch, vitality, spirit"
abilities_mid:
  - name: "Natural Invisibility"
    desc: "A poltergeist is naturally [[Invisible]]. It becomes visible only when it uses Frighten."
  - name: "Rejuvenation"
    desc: "When a poltergeist is destroyed, it reforms, fully healed, where it was destroyed after 2d4 days. A poltergeist can be permanently destroyed only if someone determines the reason for its existence and sets right whatever prevents the spirit from resting."
  - name: "Telekinetic Defense"
    desc: "`pf2:r` **Trigger** A creature approaches within 10 feet of the poltergeist <br>  <br> **Effect** The poltergeist makes a telekinetic object Strike against the triggering creature."
speed: "0 feet"
attacks:
  - name: "Ranged strike"
    desc: "Telekinetic Object +13 (`pf2:1`) (magical, occult, range 60 ft.), **Damage** 2d12 untyped"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 23, attack +13<br>**2nd** [[Telekinetic Maneuver]] (At Will)<br>**1st** [[Telekinetic Hand]]"
abilities_bot:
  - name: "Frighten"
    desc: "`pf2:1` **Requirements** The poltergeist must be [[Invisible]] <br>  <br> **Effect** The poltergeist becomes visible, appearing as a skeletal, ghostlike humanoid. Each creature within 30 feet must attempt a DC 21 [[Will]] save, becoming [[Frightened]] 2 on a failure. On a critical failure, it's also [[Fleeing]] for as long as it's frightened. On a success, the creature is temporarily immune for 1 minute. <br>  <br> At the start of its next turn, the poltergeist becomes invisible again."
  - name: "Telekinetic Storm"
    desc: "`pf2:2` The poltergeist telekinetically throws numerous small objects, such as dozens of pieces of silverware or books, either spreading them out among multiple foes or directing them at one target. <br>  <br> - When this effect is spread out among multiple foes, the poltergeist makes a telekinetic object Strike at a -2 penalty against each creature within @Template[emanation|distance:30]{30 feet}. These count as one attack for the poltergeist's multiple attack penalty, and the penalty doesn't increase until after all the attacks. <br>  <br> - When this effect has only one target, the poltergeist makes a telekinetic object Strike against the target, and the damage increases to 3d12. It deals 1d12 untyped damage on a failure, and no damage on a critical failure."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

When a creature dies, and for whatever reason its spirit is unable or unwilling to leave the site of its death, that spirit may manifest as a poltergeist: a restless, invisible spirit that is still able to manipulate physical objects. Many poltergeists perished in a way that resulted from or led to extreme emotional trauma.

```statblock
creature: "Poltergeist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
