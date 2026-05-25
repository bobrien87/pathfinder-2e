---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gunsmith"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +4, Crafting +13, Society +5, Firearm Lore +13"
abilityMods: ["+1", "+3", "+0", "+2", "+3", "+0"]
abilities_top:
  - name: "Firearm Specialist"
    desc: "For encounters involving the crafting or maintenance of firearms, the gunsmith is a 6th-level challenge."
  - name: "Misfires"
    desc: "Firearms that are improperly maintained or subjected to unusual strain can misfire. If a creature attempts to fire a firearm that was fired the previous day or earlier and hasn't been cleaned since, it rolls a DC 5 flat check before making its attack roll. If it fails this misfire check, the weapon misfires and jams. The attack is an automatic critical failure, and a creature must use an Interact action to clear the jam before the weapon can be reloaded and fired again. Once a creature has spent at least an hour cleaning a weapon, no one needs to roll for a misfire for that weapon until the next day unless an effect says otherwise."
  - name: "Crafty Reload"
    desc: "The gunsmith can Interact to reload a firearm without a free hand if they have a firearm in each hand. In addition, each time the gunsmith reloads a firearm, they can attempt a [[Crafting]] check against the hard DC for the firearm's level (DC 17 [[Crafting]] check for a dueling pistol). On a success, they gain a +1 circumstance bonus on the next attack roll they make with that firearm before the start of their next turn."
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "16"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +8 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
  - name: "Ranged strike"
    desc: "Dueling Pistol +8 (`pf2:1`) (concealable, concussive, fatal d10, reload 1, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Firearm Sabotage"
    desc: "`pf2:1` **Requirements** The gunsmith is wielding or holding a one-handed firearm and has a free hand <br>  <br> **Effect** The gunsmith deftly makes a minor modification to a firearm that can be detected with a [[Perception]] check opposed by the gunsmith's Crafting DC. If the sabotage is not reversed with a successful Crafting check against the gunsmith's Crafting DC, the firearm automatically misfires the next time it is used (the flat check is an automatic failure; see the Misfires sidebar)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Even though every gunslinger learns the basics of maintaining and repairing firearms as a part of their training, few would question the expertise of a master gunsmith regarding the weapons by which they live and die. Although professional gunsmiths are rarely found outside of settlements where firearms are common, such as Alkenstar or Dongun Hold, true masters of this specialized craft tend to quickly build reputations for themselves that extend well beyond the borders of whatever region they call home.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Gunsmith"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
