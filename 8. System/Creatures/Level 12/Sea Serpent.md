---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sea Serpent"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +18, Athletics +26, Stealth +28"
abilityMods: ["+8", "+4", "+6", "-4", "+2", "+0"]
abilities_top:
  - name: "Undetectable"
    desc: "A sea serpent automatically tries to counteract any detection, revelation, or scrying divination attempted against it, using its [[Stealth]] check modifier for its counteract modifier."
  - name: "Sea Serpent Algae"
    desc: "The water in the ballast organs around the sea serpent's neck is full of psychotropic algae. <br>  <br> **Saving Throw** DC 34 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Confused]] and, if flying, spends its first action each turn to descend 20 feet (1 round) <br>  <br> **Stage 2** confused and, if flying, descends until reaching the ground or water below (1 round)"
armorclass:
  - name: AC
    desc: "35; **Fort** +25, **Ref** +21, **Will** +21"
health:
  - name: HP
    desc: "210"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +27 (`pf2:1`) (reach 20 ft., unarmed), **Damage** 3d10+14 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail +27 (`pf2:1`) (agile, reach 30 ft.), **Damage** 2d10+14 bludgeoning plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Water Spout +25 (`pf2:1`) (brutal, water, range 100 ft.), **Damage** 2d6+12 bludgeoning plus [[Sea Serpent Algae]]"
spellcasting: []
abilities_bot:
  - name: "Capsize"
    desc: "`pf2:1` The sea serpent attempts to capsize an aquatic vessel of its size or smaller that it's adjacent to. It must succeed at an DC 35 [[Athletics]] check with a DC of 35 (reduced by 5 for each size smaller than the sea serpent) or the pilot's Sailing Lore DC, whichever is higher."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d10+14)[bludgeoning]], DC 32 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Spine Rake"
    desc: "`pf2:2` The sea serpent extends the spines along its back and Swims or Strides. Each creature the serpent is adjacent to at any point during its movement takes @Damage[(4d6+8)[slashing]] damage (DC 32 [[Reflex]] save)."
  - name: "Swallow Whole"
    desc: "`pf2:1` Huge, @Damage[(2d10+6)[bludgeoning]], Rupture 20 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These fabled beasts resemble massive snakes with long rows of finned spines down their back. Temperamental and territorial, sea serpents can capsize a boat with ease, and most won't hesitate to do so when hungry or threatened. Stories abound of aggrieved captains who spend their entire lives hunting down the elusive monster that sunk their ships and took their livelihoods. These hunts rely on rumors and glimpses of the beasts, as few survive the catastrophes wrought by sea serpents.

While many fishermen's tales paint sea serpents as divinely appointed guardians of the ocean or as evil and demonic agents, the truth is that most sea serpents are simply very large beasts with a knack for avoiding magical detection.

```statblock
creature: "Sea Serpent"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
