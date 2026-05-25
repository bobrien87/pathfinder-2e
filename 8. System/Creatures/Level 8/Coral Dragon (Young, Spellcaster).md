---
type: creature
group: ["Amphibious", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Coral Dragon (Young, Spellcaster)"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Primal"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]], [[Wavesense]] (imprecise) 60 feet"
languages: "Common, Draconic, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +16, Diplomacy +18, Intimidation +18, Nature +16, Society +14, Stealth +16, Survival +16"
abilityMods: ["+6", "+2", "+4", "+2", "+2", "+6"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +18, **Ref** +14, **Will** +15"
health:
  - name: HP
    desc: "135; **Immunities** dazzled, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Primal"
    desc: ""
  - name: "Biomineralize"
    desc: "`pf2:r` **Trigger** The dragon is critically hit by a melee weapon without reach or an unarmed attack that deals slashing or piercing damage <br>  <br> **Effect** A gout of blood spurts from the dragon's wound and instantaneously calcifies into a jagged branch of sharpened coral. The coral branch impales the triggering creature, dealing 5d6 piercing damage (DC 26 [[Reflex]] save). The triggering creature also takes 1d4 persistent,bleed damage on a critical failure. Regardless of the outcome, the coral then crumbles to dust."
  - name: "Reef Bond"
    desc: "Every coral dragon is mystically bound to a single living coral reef. If the dragon moves more than 3 miles from their reef, they become [[Sickened]] 1 and unable to recover, with the sickened value increasing by 1 every 6 hours unless they succeed at a DC 28 [[Fortitude]] save. After 24 hours, the dragon becomes [[Drained]] 1; its drained value increases by 1 every 24 hours. <br>  <br> If the dragon's reef suffers significant damage, they immediately become aware of the location where the reef was harmed but not the source or nature of the damage. Should the reef ever be completely destroyed, the dragon is immediately slain."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+10 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, magical), **Damage** 2d6+10 slashing"
  - name: "Melee strike"
    desc: "Tail +18 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d8+10 bludgeoning plus [[Knockdown]]"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 26, attack +18<br>**4th** (2 slots) [[Hydraulic Torrent]], [[Vapor Form]]<br>**3rd** (3 slots) [[Aqueous Orb]], [[Crashing Wave]], [[Slow]]<br>**2nd** (3 slots) [[Mist]], [[Water Breathing]], [[Water Walk]]<br>**1st** (3 slots) [[Air Bubble]], [[Create Water]], [[Tailwind]]<br>**Cantrips** [[Detect Magic]], [[Know the Way]], [[Prestidigitation]], [[Spout]], [[Stabilize]]"
abilities_bot:
  - name: "Hydraulic Breath"
    desc: "`pf2:2` The dragon exhales a pressurized jet of water that deals @Damage[9d6[bludgeoning]|options:area-damage] damage in an @Template[type:line|distance:80] (DC 26 [[Reflex]] save). Creatures that critically fail their Reflex save against the Hydraulic Breath are pushed back 10 feet and knocked [[Prone]]. The dragon can't use Hydraulic Breath again for 1d4 rounds."
  - name: "Reef Meld"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Requirements** The coral dragon is in physical contact with their bound reef <br>  <br> **Effect** The dragon physically merges with the reef and vanishes, along with up to two willing creatures, into an extradimensional space where it can neither affect nor be affected by the outside world. The effect lasts indefinitely or until the dragon Dismisses it. Once merged, the dragon can spend 1 minute traveling to and emerging from any point on its reef up to 1 mile away."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Coral dragons are the primal guardians of the vast living coral reefs found in oceans across Golarion. Even by draconic standards, coral dragons stand out for their arrogance and vanity, boasting inordinate pride in the vibrant hues of their own coral-encrusted scales and the dazzling splendor of the reefs they protect. Coral dragons like to decorate their reefs, which they view as lairs, with objects of beauty, dotted with the occasional bit of valuables like coins. Those who seek the favor of a coral dragon often find the creature easily swayed by flattery, particularly when paired with shiny or brightly colored gifts that complement the scintillating beauty of the dragon and their underwater domain.

```statblock
creature: "Coral Dragon (Young, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
