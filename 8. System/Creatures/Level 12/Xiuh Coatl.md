---
type: creature
group: ["Beast", "Couatl"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Xiuh Coatl"
level: "12"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Couatl"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; [[Darkvision]], [[Thoughtsense]] (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +21, Arcana +23, Diplomacy +26, Intimidation +26, Nature +23, Occultism +23, Society +21, Stealth +21, Survival +21"
abilityMods: ["+7", "+3", "+4", "+5", "+5", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Thoughtsense (Imprecise) 60 feet"
    desc: "Thoughtsense allows a monster to sense all non-mindless creatures at the listed range."
  - name: "Xiuh Coatl Venom"
    desc: "To unholy creatures, this is a curse instead of a poison and deals spirit damage instead of poison damage <br>  <br> **Saving Throw** DC 32 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d8 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d10 poison damage, enfeebled 1, and –5-foot status penalty to all Speeds (1 round) <br>  <br> **Stage 3** 3d8 poison damage, [[Enfeebled]] 2, and –10-foot status penalty to all Speeds (1 round) <br>  <br> Against unholy <br>  <br> **Saving Throw** DC 32 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d8 spirit damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d10 spirit damage, enfeebled 1, and –5-foot status penalty to all Speeds (1 round) <br>  <br> **Stage 3** 3d8 spirit damage, [[Enfeebled]] 2, and –10-foot status penalty to all Speeds (1 round)"
armorclass:
  - name: AC
    desc: "33; **Fort** +20, **Ref** +19, **Will** +25"
health:
  - name: HP
    desc: "220; **Immunities** electricity, fire; **Weaknesses** cold 8"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +25 (`pf2:1`) (magical, unarmed), **Damage** 2d10+10 piercing plus 2d8 fire plus [[Grab]] plus [[Xiuh Couatl Venom]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 32, attack +24<br>**7th** [[Interplanar Teleport]]<br>**5th** [[Illusory Scene]], [[Sending]], [[Wave of Despair]]<br>**4th** [[Clairvoyance]]<br>**3rd** [[Clairaudience]], [[Dream Message]], [[Mind Reading]] (At Will), [[Ring of Truth]]<br>**2nd** [[Dispel Magic]], [[Invisibility (self only, at will)]], [[See the Unseen]]<br>**1st** [[Charm]], [[Detect Magic]], [[Fear]], [[Figment]], [[Mindlink]], [[Phantom Pain]], [[Read Aura]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Greater Constrict"
    desc: "`pf2:1` @Damage[(1d10+10)[bludgeoning],1d8[electricity]]{1d10+10 bludgeoning plus 1d8 electricity}, DC 32 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC. A creature that fails this save falls [[Unconscious]], and a creature that succeeds is then temporarily immune to falling unconscious from Greater Constrict for 1 minute."
  - name: "Instrument of Retribution"
    desc: "`pf2:3` The xiuh coatl transforms into any simple or martial weapon. The weapon is always a *+2 greater striking flaming shock weapon* and can be of any size, chosen by the xiuh coatl when they transform. In weapon form, the xiuh coatl gains Hardness equal to that of the weapon into which they transform, and they retain their Hit Points, saving throws, senses, telepathy, and traits while in weapon form. The xiuh coatl can Sustain to revert to their normal form."
  - name: "Volcanic Lightning Breath"
    desc: "`pf2:2` The xiuh coatl breathes a gout of flame and lightning in an @Template[type:line|distance:80] that deals @Damage[5d8[electricity],5d8[fire]|options:area-damage]{5d8 electricity damage and 5d8 fire damage} (DC 32 [[Reflex]] save). The xiuh coatl can't use Volcanic Lightning Breath again for 1d4 rounds."
  - name: "Wrap in Coils"
    desc: "`pf2:1` **Requirements** The xiuh coatl has a Medium or smaller creature [[Grabbed]] or [[Restrained]] in their jaws <br>  <br> **Effect** The mix coatl moves the creature into their coils, freeing their jaws to make attacks, and then uses [[Constrict]] against the creature. The mix coatl can hold as many creatures in their coils as will fit in their space."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Fiercer than other coatls, xiuh coatls (pronounced "shoo") are dedicated to seeking out malevolent creatures and offering a final opportunity at redemption.

Coatls are serpentine celestials who tirelessly help mortals reach their greatest potential all across the planes. Some serve benevolent deities as intermediaries, while others serve the cause of good as they see fit.

```statblock
creature: "Xiuh Coatl"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
