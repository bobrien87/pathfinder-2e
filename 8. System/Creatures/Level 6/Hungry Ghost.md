---
type: creature
group: ["Ghost", "Incorporeal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hungry Ghost"
level: "6"
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
    desc: "+13; [[Darkvision]]"
languages: "Common, Necril (One other language)"
skills:
  - name: Skills
    desc: "Deception +14, Diplomacy +14, Religion +15"
abilityMods: ["-5", "+5", "+0", "+4", "+5", "+4"]
abilities_top:
  - name: "Living Visage"
    desc: "While they have more than 30 HP, the hungry ghost appears to be a living creature. They have an automatic result of 34 on Deception checks and DCs to conceal their undead status and can Feed on the Living covertly."
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +15, **Will** +15"
health:
  - name: HP
    desc: "60; rejuvenation, void healing; **Immunities** bleed, death effects, disease, paralyzed, poison, precision, unconscious; **Resistances** all damage 5 except force, ghost touch, spirit, vitality"
abilities_mid:
  - name: "Feed on the Living"
    desc: "`pf2:2` The hungry ghost touches a living creature in reach to steal its life force. If the ghost is in their living visage, they can disguise Feed on the Living as a benign touch and delay the effects for up to 1 minute while keeping the target unaware of the effect. A creature can be affected by only one delayed Feed on the Living at a time, and if the ghost loses their living visage during that minute, the delayed effect is lost. When Feed on the Living takes effect, the target takes @Damage[(2d8+4)[void]] damage, depending on the result of its DC 24 [[Fortitude]] save. <br> - **Critical Success** The target's life energy overpowers the ghost. The hungry ghost takes 5 vitality damage, and the target is unaffected. <br> - **Success** The target takes half damage, and the hungry ghost regains HP equal to the damage dealt. <br> - **Failure** The target takes full damage and is [[Enfeebled]] 1 for 1 minute, and the hungry ghost regains HP equal to the damage dealt. <br> - **Critical Failure** The target takes double damage and is [[Enfeebled]] 2 for 1 minute, and the hungry ghost regains HP equal to the damage dealt."
  - name: "Ravenous Undoing"
    desc: "In each 24-hour period, the hungry ghost must use Feed on the Living to consume 30 HP (any HP the ghost would gain count toward this total, even if the ghost has enough HP that they don't actually regain the full amount). If the ghost hasn't consumed enough HP, they mindlessly and recklessly feed on any living creature they come across until satiated."
  - name: "Rejuvenation"
    desc: "When a hungry ghost is destroyed, they reform after 2d4 days fully healed at the location where they were last destroyed. They're only permanently destroyed when they have been given a proper burial, have had their grave cleaned and maintained for at least a year, or have been judged to be redeemed by Pharasma."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ghostly Touch +17 (`pf2:1`) (agile, finesse, magical, unarmed), **Damage** 2d8+4 void"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Hungry ghosts arise from those who didn't receive proper burials or whose graves were neglected. They are not bound to a site or item but are compelled to see opportunities to commit good deeds in hopes of gaining favors that can aid them in achieving a final rest. Their need to feed on living energy often conflicts with this goal, however.

Tethered to the world after death by powerful emotions that haven't been resolved, ghosts haunt the living as sad echoes of their former selves. Rules for creating a ghost start on page 160 of Monster Core.

```statblock
creature: "Hungry Ghost"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
