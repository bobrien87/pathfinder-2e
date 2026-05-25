---
type: creature
group: ["Aquatic", "Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kraken"
level: "18"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Aquatic"
trait_02: "Beast"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+34; [[Darkvision]]"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +38, Intimidation +32, Nature +35, Stealth +33"
abilityMods: ["+9", "+4", "+9", "+5", "+6", "+5"]
abilities_top:
  - name: "Kraken Ink"
    desc: "Krakens are immune to this poison <br>  <br> **Saving Throw** DC 39 [[Fortitude]] save; <br>  <br> **Maximum Duration** 10 rounds <br>  <br> **Stage 1** 4d6 poison damage and [[Sickened]] 1 (1 round) <br>  <br> **Stage 2** 5d6 poison damage and [[Sickened]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "42; **Fort** +35, **Ref** +28, **Will** +32"
health:
  - name: HP
    desc: "360; **Immunities** controlled, emotion; **Resistances** cold 10, poison 20"
abilities_mid:
  - name: "Altered Weather"
    desc: "A kraken reshapes the weather within 2 miles of it, with the effect of the [[Control Weather]] ritual centered on the kraken and based on its emotional state, at the GM's discretion. If the kraken dies, the weather returns to normal immediately."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Arm +37 (`pf2:1`) (magical, reach 40 ft.), **Damage** 4d10+17 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tentacle +37 (`pf2:1`) (agile, magical, reach 60 ft., unarmed), **Damage** 3d10+17 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Beak +37 (`pf2:1`) (magical, reach 20 ft., unarmed), **Damage** 3d10+17 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 40, attack +32<br>**8th** [[Punishing Winds]]<br>**6th** [[Dominate (Animals Only)]]<br>**2nd** [[Resist Energy]]"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d10+17)[bludgeoning]], DC 40 [[Fortitude]] save. On a failed save, a creature that is holding its breath loses 1d4 rounds worth of air. <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Double Attack"
    desc: "`pf2:1` The kraken makes two Strikes with two different arms or tentacles, each limb targeting a different creature. Double Attack counts as two attacks toward the kraken's multiple attack penalty, but the penalty doesn't increase until after both attacks are made. <br>  <br> If the kraken subsequently uses the Grab action, it Grabs any number of creatures it hit with Double Attack."
  - name: "Ink Cloud"
    desc: "`pf2:1` The kraken releases a cloud of black, venomous ink in an @Template[emanation|distance:80]. This cloud has no effect outside water. <br>  <br> Creatures inside the ink cloud are exposed to kraken ink poison and are [[Undetected]] while inside the cloud. <br>  <br> The kraken can't use Ink Cloud again for 2d6 rounds, and the cloud dissipates after 1 minute."
  - name: "Jet"
    desc: "`pf2:1` The kraken moves through the water up to 280 feet in a straight line without triggering reactions."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A kraken is an enormous, squid-like leviathan with a cruel intelligence. It hunts ships, whales, and heroes alike. The hatred and envy krakens hold for alghollthus, their rivals, has led many krakens to make their lairs in sunken cities, where they can sift through ancient lore and uncover long-lost arcane secrets.

```statblock
creature: "Kraken"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
