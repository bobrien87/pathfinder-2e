---
type: creature
group: ["Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Yeti"
level: "5"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Humanoid"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Athletics +14, Stealth +12, Survival +11"
abilityMods: ["+5", "+2", "+4", "-1", "+4", "-1"]
abilities_top:
  - name: "Snowblind"
    desc: "When [[Hiding]], the yeti is [[Concealed]] by any snowfall, even if it's not thick enough to make other creatures concealed."
  - name: "Arctic Passage"
    desc: "The yeti ignores difficult terrain caused by ice or snow."
armorclass:
  - name: AC
    desc: "21; **Fort** +15, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "115; **Immunities** cold; **Weaknesses** fire 10"
abilities_mid:
  - name: "Nightmare Guardian"
    desc: "Yetis gain a +4 status bonus to saves against fear and against spells and abilities that affect dreams. A yeti that falls prey to a supernatural nightmare loses this ability and becomes permanently enraged, gaining a +1 status bonus to attack and damage rolls and a -1 status penalty to AC."
  - name: "Vanish"
    desc: "`pf2:r` **Trigger** The yeti is [[Hidden]] or [[Undetected]] while not in combat, and a creature would observe it. <br>  <br> **Effect** The yeti Strides or Climbs up to half its Speed to a location where it can [[Hide]], then Hides. If its new Stealth check result meets or exceeds the triggering creature's Perception DC, the yeti remains hidden."
  - name: "Grizzly Arrival"
    desc: "`pf2:0` **Trigger** The yeti hits a creature in the first round of combat and the yeti was [[Hidden]] from that creature at the start of combat. <br>  <br> **Effect** Each enemy within @Template[emanation|distance:30]{30 feet} that witnesses the attack (including the target of the attack) must attempt a DC 23 [[Will]] save. On a failure, the creature is [[Frightened]] 2; on a critical failure, it's [[Frightened]] 4."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +15 (`pf2:1`) (unarmed), **Damage** 2d10+5 slashing"
spellcasting: []
abilities_bot:
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Nearly a myth, a yeti is rarely seen—and even when it is, it is often too late. Yetis dwell amid the highest, most remote peaks of the world, coming down from their snowy mountain holds to raid, steal livestock, and sometimes feed their insatiable urges for slaughter and destruction. Those folks who live at the foot of a yeti-ruled mountain warn of the "abominable snowmen": monstrous, furcovered humanoids who leave strange and bloody tracks in the snow.

In actuality, most yetis protect the world rather than hunt its other denizens, guarding eldritch portals that link the mortal Universe and other, much stranger dimensions of reality. From within these snow-covered arches and ancient stone doorways, aliens, living nightmares, fiends, and worse can emerge into the world. Yetis who guard these portals sometimes succumb to the horrors within, taking on the bloodthirsty urges and horrific behaviors of the very monsters they strive to guard against. Driven out of their clans and forced to wander alone, they give rise to the myth of the abominable snowman. These exiled yetis often fully embrace the corrupting elements that caused their exile in the first place, growing more powerful and more deadly.

```statblock
creature: "Yeti"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
