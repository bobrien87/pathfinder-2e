---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Moray Eel"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +13, Stealth +13"
abilityMods: ["+6", "+2", "+3", "-4", "+2", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +14, **Ref** +13, **Will** +9"
health:
  - name: HP
    desc: "65; **Resistances** bludgeoning 5, piercing 5"
abilities_mid:
  - name: "Ambush"
    desc: "`pf2:r` **Trigger** A target creature passes within 20 feet of the giant moray eel's hiding place and has not detected the giant moray eel <br>  <br> **Effect** The giant moray eel lunges out of its hiding place, Swims directly toward the triggering creature, and makes a jaws Strike against it. The target creature is [[Off Guard]] to this attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d6+8 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Pharyngeal Jaws"
    desc: "`pf2:2` **Requirements** The giant moray eel has a creature [[Grabbed]] in its jaws <br>  <br> **Effect** The giant moray eel uses its second set of jaws to pull the prey into its gullet. The eel deals @Damage[(1d6+4)[piercing]] damage to the grabbed creature and gains a +2 circumstance bonus to its Swallow Whole attempts and to the DC for the creature to [[Escape]]. This effect ends if the target Escapes or the giant moray eel Swallows it Whole."
  - name: "Swallow Whole"
    desc: "`pf2:1` Small, @Damage[(1d6+6)[bludgeoning]], Rupture 12 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Giant moray eels dwell in warm, tropical waters and build lairs in narrow, twisting caves made of coral. Their size, speed, and powerful bite make them dangerous to divers and fishers. Giant moray eels have rubbery hides that secrete a layer of mucus, making them difficult to harm with some weapons.

Although these long, narrow fish share similarities in appearance, eels are a diverse group of creatures.

```statblock
creature: "Giant Moray Eel"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
