---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phasmadaemon"
level: "17"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+29; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Common, Daemonic (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +31, Deception +31, Intimidation +33, Religion +29"
abilityMods: ["+8", "+8", "+6", "+3", "+4", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Inescapable Form"
    desc: "The phasmadaemon can Squeeze through tight spaces as if it were a Small creature. While Squeezing, it can move at its full Speed. The phasmadaemon can even Squeeze through spaces that typically fit only a Tiny creature, but does so at the standard speed for Squeezing."
armorclass:
  - name: AC
    desc: "39; **Fort** +31, **Ref** +26, **Will** +31"
health:
  - name: HP
    desc: "340; **Immunities** death effects, fear effects; **Weaknesses** holy 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Frightful Presence"
    desc: "60 feet. DC 35 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Unending Terror"
    desc: "Escaping fear near a phasmadaemon is no simple task. Creatures don't automatically reduce their [[Frightened]] condition while they are within the phasmadaemon's Frightful Presence aura. Instead, they must attempt a Will save at the end of their turn against the DC of the effect that caused the condition. On a success, the creature's frightened condition is reduced by 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +33 (`pf2:1`) (magical, reach 10 ft., unarmed, unholy), **Damage** 3d10+19 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +33 (`pf2:1`) (agile, magical, reach 10 ft., unarmed, unholy), **Damage** 3d8+19 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30<br>**9th** [[Phantasmagoria]]<br>**7th** [[Duplicate Foe]], [[Mask of Terror]]<br>**6th** [[Truesight]] (Constant)<br>**5th** [[Shadow Blast]], [[Shadow Blast]], [[Shadow Blast]]<br>**4th** [[Nightmare]] (At Will), [[Translocate]], [[Translocate]] (At Will), [[Vision of Death]]"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(3d10+9)[bludgeoning]], DC 35 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Consume Fear"
    desc: "`pf2:1` **Requirements** The phasmadaemon has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The phasmadaemon feeds on the creature's mortality and innate terror, dealing 6d8 mental damage. The creature must attempt a DC 38 [[Will]] save. <br> - **Critical Success** The creature takes no damage and manages to break free from the phasmadaemon's Grab. <br> - **Success** The creature takes half damage. <br> - **Failure** The creature takes full damage and increases their frightened conditioned by 1, to a maximum of [[Frightened]] 4. <br> - **Critical Failure** The creature takes double damage and increases their frightened condition by 2, to a maximum of frightened 4. If the creature is already frightened 4, it must attempt a DC 38 [[Fortitude]] save saving throw. If it fails, it's reduced to 0 Hit Points and dies. This effect has the death and incapacitation traits."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The horrifying phasmadaemons make use of illusions and their own frightening appearances (that of serpents with bony tails, horned crocodilian skulls for heads, and several insectile pincers) to strike fear into the hearts of others. They represent deaths brought about by fright. Ultimately, any kind of fear can lead to the creation of a phasmadaemon, but a soul who transforms into such a fiend must quickly find other fears to feed on to build up their own strength. Without the nourishment of human fear, the newborn phasmadaemon begins to waste away, eventually "dying" and becoming planar quintessence. Only the most clever and capable phasmadaemons survive their initial hunger, learning how to prey on even the bravest souls as a result.

```statblock
creature: "Phasmadaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
