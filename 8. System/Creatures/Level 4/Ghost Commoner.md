---
type: creature
group: ["Ghost", "Incorporeal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ghost Commoner"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Ghost"
trait_02: "Incorporeal"
trait_03: "Spirit"
trait_04: "Undead"
trait_05: "Unholy"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Stealth +12, Dwelling Lore (applies to the place the ghost is bound to) +10"
abilityMods: ["-5", "+3", "+0", "+0", "+2", "+2"]
abilities_top:
  - name: "Site Bound"
    desc: "A typical ghost can stray only a short distance from where it was killed or the place it haunts. A typical limit is 120 feet. Some ghosts are instead bound to a room, building, item, or creature that was special to it rather than a location."
armorclass:
  - name: AC
    desc: "20; **Fort** +8, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "30; rejuvenation, void healing; **Immunities** death effects, disease, paralyzed, poison, precision, unconscious, bleed; **Resistances** all damage 5 except force, ghost touch, spirit, vitality"
abilities_mid:
  - name: "Rejuvenation"
    desc: "Setting right the injustice that led to the commoner's death allows it to move on to the afterlife. <br>  <br> When a ghost is destroyed, it re-forms after 2d4 days within the location it's bound to, fully healed. A ghost can be permanently destroyed only if someone determines the reason for its existence and sets right whatever prevents the spirit from resting."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ghostly Hand +13 (`pf2:1`) (agile, finesse, magical), **Damage** 2d6+2 void"
spellcasting: []
abilities_bot:
  - name: "Frightful Moan"
    desc: "`pf2:1` The ghost laments its fate, forcing each living creature within @Template[emanation|distance:30]{30 feet} to attempt a DC 21 [[Will]] save. On a failure, a creature becomes [[Frightened]] 2 (or [[Frightened]] 3 on a critical failure). On a success, a creature is temporarily immune to this ghost's frightful moan for 1 minute."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The ghost commoner is an ordinary person who believes they died unjustly.

When some mortals die through tragic circumstances or without closure, their souls can linger and haunt a locale significant to them in life.

```statblock
creature: "Ghost Commoner"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
